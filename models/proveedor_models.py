from pydantic import BaseModel

class ProveedorIn(BaseModel):
    nitprov: int
    razon_social_prov: str
    direccion_prov: str
    telefono_prov: str
    ciudad_prov: str
    paginaweb_prov: str
    correo_prov: str
    rep_legal_prov: str
    contacto_prov: str

class ProveedorOut(BaseModel):
    nit: int
    razon_social: str
    direccion: str
    telefono: str
    ciudad: str
    paginaweb: str
    correo: str