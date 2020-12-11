from typing import  Dict
from pydantic import BaseModel

class EmpresaInDB(BaseModel):
    nit:str
    razon_social: str
    direccion: str
    telefono: str
    ciudad: str
    paginaweb: str
    correo: str
    replegal: str
    resolfacturacion: str


database_empresa = Dict[str, EmpresaInDB]

database_empresa ={
    1: EmpresaInDB(**{"nit":"901140123-8",
                        "razon_social":"Equipo 10 SAS",
                        "direccion":"",
                        "fecha_nacimiento":"12/06/1987",
                        "telefono": "55555555",
                        "ciudad":"Bogotá",
                        "paginaweb":"www.equipo10.com",
                        "correo": "contacto@equipo10.com",
                        "replegal":"01/12/2020",
                        "resolfacturacion": "111231645"})
}

def get_empresa(nit: str):
    if nit in database_empresa.keys():
        return database_empresa[razon_social]
    else:
        return None

def update_empresa(empresa_in_db: EmpresaInDB):
    database_empresa[empresa_in_db.nit_prov] = empresa_in_db
    return empresa_in_db
