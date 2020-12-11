from pydantic import BaseModel

class EmpleadoIn(BaseModel):
    usuario: str
    contrasena: str

class EmpleadoOut(BaseModel):
    usuario: str
    estado: str
