from typing import  Dict
from pydantic import BaseModel

class ProveedorInDB(BaseModel):
    nit_prov: str
    razon_social_prov: str
    direccion_prov: str
    telefono_prov: str
    ciudad_prov: str
    paginaweb_prov: str
    correo_prov: str
    rep_legal_prov: str
    contacto_prov: str

database_proveedor = Dict[str, ProveedorInDB]

database_proveedor ={
    12345: ProveedorInDB(**{"nit_prov":"12345-6",
                        "razon_social_prov":"Empresa ABC SAS",
                        "direccion_prov":"Calle Falsa 123",
                        "telefono_prov":"12345678 Ext 123",
                        "ciudad_prov":"Bogota",
                        "paginaweb_prov": "www.pagina.com",
                        "correo_prov": "proveedor@pagina.com",
                        "rep_legal_prov":"Pedro Coral",
                        "contacto_prov":"Pastor Lopez"}),

    12345: ProveedorInDB(**{"nit_prov":"2468-1",
                        "razon_social_prov":"Compumundo Hipermegared SAS",
                        "direccion_prov":"Av Real 456",
                        "telefono_prov":"6542315 Ext 5664",
                        "ciudad_prov": "Bogotá",
                        "paginaweb_prov": "www.pagina2.com",
                        "correo_prov": "proveedor@pagina2.com",
                        "rep_legal_prov":"Harry Potter",
                        "contacto_prov":"Ron Fernandez"}),


    12345: ProveedorInDB(**{"nit_prov":"2564654-1",
                        "razon_social_prov":"Bavaria",
                        "direccion_prov":"Calle 123456",
                        "telefono_prov":"6556944 Ext 5664",
                        "ciudad_prov": "Bogotá",
                        "paginaweb_prov": "www.bavaria.com",
                        "correo_prov": "proveedor@bavaria.com",
                        "rep_legal_prov":"Clark Kent",
                        "contacto_prov":"Lois Lane"}),
}

def get_proveedor(nit_prov: str):
    if nit_prov in database_proveedor.keys():
        return database_proveedor[razon_social_prov]
    else:
        return None

def update_proveedor(proveedor_in_db: ProveedorInDB):
    database_proveedor[proveedor_in_db.nit_prov] = proveedor_in_db
    return proveedor_in_db