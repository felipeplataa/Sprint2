from pydantic import BaseModel

class EmpresaIn(BaseModel):
    nit:str
    razon_social: str
    direccion: str
    telefono: str
    ciudad: str
    paginaweb: str
    correo: str
    replegal: str
    resolfacturacion: str

class EmpresaOut(BaseModel):
    nit:str
    razon_social: str
    direccion: str
    telefono: str
    ciudad: str
    paginaweb: str
    correo: str
    resolfacturacion: str