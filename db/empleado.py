from typing import  Dict
from pydantic import BaseModel

class EmpleadoInDB(BaseModel):
    usuario: str
    nombre:str
    apellido: str
    fecha_nacimiento:str
    telefono: str
    email: str
    fecha_ingreso : str
    area: str
    cargo: str
    contrasena: str
    estado: str

database_empleado = Dict[int, EmpleadoInDB]

database_empleado ={
    "fplata": EmpleadoInDB(**{"usuario":"fplata",
                        "nombre":"Felipe",
                        "apellido":"Plata",
                        "fecha_nacimiento":"12/06/1987",
                        "telefono": "3112422494",
                        "email": "andres.felipe.plata.a@gmail.com",
                        "fecha_ingreso":"01/12/2020",
                        "area":"Comercial",
                        "cargo":"Vicepresidente Junior",
                        "contrasena":"12345",
                        "estado": "activo"}),

    "aavendano": EmpleadoInDB(**{"usuario":"aavendano",
                        "nombre":"Andres",
                        "apellido":"Avendaño",
                        "fecha_nacimiento":"12/12/1993",
                        "telefono": "7101252",
                        "email": "andres.felipe@gmail.com",
                        "fecha_ingreso":"01/12/2020",
                        "area":"Financiera",
                        "cargo":"Consultor",                        
                        "contrasena":"12345",
                        "estado": "activo"}),
}

def get_empleado(usuario: str):
    if usuario in database_empleado.keys():
        return database_empleado[usuario]
    else:
        return None

def update_empleado(empleado_in_db: EmpleadoInDB):
    database_empleado[empleado_in_db.usuario] = empleado_in_db
    return empleado_in_db





