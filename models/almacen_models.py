from pydantic import BaseModel

class AlmacenIn(BaseModel):
    nombre_almacen: str
    direccion_almacen: str
    responsable_almacen: str
    tipo_almacen: str
    telefono_almacen:str

class AlmacenOut(BaseModel):
    nombre_almacen: str
    direccion_almacen: str
    responsable_almacen: str
    tipo_almacen: str
    telefono_almacen:str