from typing import  Dict
from pydantic import BaseModel

class AlmacenInDB(BaseModel):
    nombre_almacen: str
    direccion_almacen: str
    responsable_almacen: str
    tipo_almacen: str
    telefono_almacen:str

database_almacen = Dict[str, AlmacenInDB]

database_almacen = {
    "almacenBogota": AlmacenInDB(**{"nombre_almacen":"AlmacenBogota",
                                        "direccion_almacen":"Cra 12#34-56",
                                        "responsable_almacen":"Felipe Plata",
                                        "tipo_almacen":"Bodega",
                                        "telefono_almacen":"8765431"}),

    "almacenMedellin": AlmacenInDB(**{"nombre_almacen":"AlmacenMedellin",
                                        "direccion_almacen":"Cra 34#56-78",
                                        "responsable_almacen":"Felipe Plata",
                                        "tipo_almacen":"Punto de Venta",
                                        "telefono_almacen":"9654321"}),
}

def get_almacen(nombre_almacen: str):
    if nombre_almacen in database_almacen.keys():
        return database_almacen[nombre_almacen]
    else:
        return None

def update_almacen(almacen_in_db: AlmacenInDB):
    database_almacen[almacen_in_db.nombre_almacen] = almacen_in_db
    return almacen_in_db