from typing import  Dict
from pydantic import BaseModel

class ClienteInDB(BaseModel):
    identificacion_cliente: str
    tipo_de_identificacion_cliente: str
    nombre_cliente: str    
    direccion_cliente: str
    correo_electronico_cliente:str
    telefono_cliente: str

database_cliente = Dict[str, ClienteInDB]

database_cliente ={
    "1019123456": ClienteInDB(**{"identificacion_cliente":"1019123456",
                                    "tipo_de_identificacion_cliente":"Cédula de ciudadania",
                                    "nombre_cliente":"Ace Ventura",
                                    "direccion_cliente":"Calle 1234",
                                    "correo_electronico_cliente":"aceventura@gmail.com",
                                    "telefono_cliente":"3211234567"}),

    "555555555-9": ClienteInDB(**{"identificacion_cliente":"555555555-9",
                                    "tipo_de_identificacion_cliente":"Nit",
                                    "nombre_cliente":"Heets SAS",
                                    "direccion_cliente":"Cra 987654",
                                    "correo_electronico_cliente":"heets@gmail.com",
                                    "telefono_cliente":"55555564"}),

    "1012055555": ClienteInDB(**{"identificacion_cliente":"1012055555",
                                    "tipo_de_identificacion_cliente":"Cédula de ciudadania",
                                    "nombre_cliente":"Bruce Wayne",
                                    "direccion_cliente":"Mansion Wayne",
                                    "correo_electronico_cliente":"batman@gmail.com",
                                    "telefono_cliente":"9996532"}),
}

def get_cliente(identificacion_cliente: str):
    if identificacion_cliente in database_cliente.keys():
        return database_cliente[identificacion_cliente]
    else:
        return None

def update_cliente(cliente_in_db: ClienteInDB):
    database_cliente[cliente_in_db.identificacion_cliente] = cliente_in_db
    return cliente_in_db

