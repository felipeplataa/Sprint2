from db.almacen import AlmacenInDB, get_almacen,update_almacen
from db.cliente import ClienteInDB,get_cliente,update_cliente
from db.empleado import EmpleadoInDB,get_empleado,update_empleado
from db.empresa import EmpresaInDB, get_empresa, update_empresa
from db.factura import FacturaInDB, save_factura
from db.producto import ProductoInDB, get_producto,update_producto
from db.proveedor import ProveedorInDB, get_proveedor, update_proveedor
from db.inventario import InventarioInDB,save_entrada, save_salida, database_entrada, database_salida 
from db.producto import database_producto
from db.cliente import database_cliente
from models.almacen_models import AlmacenIn, AlmacenOut
from models.cliente_models import ClienteIn, ClienteOut
from models.empleado_models import EmpleadoIn, EmpleadoOut
from models.empresa_models import EmpresaIn, EmpresaOut
from models.factura_models import FacturaIn, FacturaOut
from models.producto_models import ProductoIn, ProductoOut
from models.proveedor_models import ProveedorIn, ProveedorOut
from models.inventario_models import SalidaIn, SalidaOut, EntradaIn, EntradaOut

import datetime
from fastapi import FastAPI, HTTPException


api = FastAPI()




@api.get("/producto/")
async def producto():
    return{"message": database_producto}    


@api.get("/producto/codigo/{codigo_prod}")
async def get_productos(codigo_prod: str):

    producto_in_db = get_producto(codigo_prod)

    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe en el sistema")

    producto_out = ProductoOut(**producto_in_db.dict())

    return  producto_out

@api.put("/producto/entrada/")
async def ingreso_producto(entradaInventario_in: EntradaIn):

    producto_in_db = get_producto(entradaInventario_in.codigo_prod)

    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no ha sido creado")


    producto_in_db.costo_unit_prod = (((producto_in_db.cantidad_prod*producto_in_db.costo_unit_prod)+(entradaInventario_in.cantidad_prod*entradaInventario_in.costo_prod_ent))/(producto_in_db.cantidad_prod + entradaInventario_in.cantidad_prod))
    producto_in_db.cantidad_prod = producto_in_db.cantidad_prod + entradaInventario_in.cantidad_prod

    update_producto(producto_in_db)


    entradaInventario_in_db = InventarioInDB(**entradaInventario_in.dict(), cantidad_actual= producto_in_db.cantidad_prod, costo_actual=producto_in_db.costo_unit_prod)
    entradaInventario_in_db = save_entrada(entradaInventario_in_db)

    entradaInventario_out = EntradaOut(**entradaInventario_in_db.dict())

    return  entradaInventario_out

@api.put("/producto/salida/")
async def salida_producto(salidaInventario_in: SalidaIn):

    producto_in_db = get_producto(salidaInventario_in.codigo_prod)

    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no ha sido creado")

    if producto_in_db.cantidad_prod < salidaInventario_in.cantidad_prod:
        raise HTTPException(status_code=400, detail="No hay suficiente stock de inventario")


    producto_in_db.cantidad_prod = producto_in_db.cantidad_prod - salidaInventario_in.cantidad_prod
    update_producto(producto_in_db)

    salidaInventario_in_db = InventarioInDB(**salidaInventario_in.dict(), cantidad_actual= producto_in_db.cantidad_prod, costo_actual=producto_in_db.costo_unit_prod, costo_prod_ent=0)
    salidaInventario_in_db = save_salida(salidaInventario_in_db)

    salidaInventario_out = SalidaOut(**salidaInventario_in_db.dict())

    return  salidaInventario_out



