from pydantic import BaseModel

class ClienteIn(BaseModel):
    identificacion_cliente: str
    tipo_de_identificacion_cliente: str
    nombre_cliente: str    
    direccion_cliente: str
    correo_electronico_cliente:str
    telefono_cliente: str

class ClienteOut(BaseModel):
    identificacion_cliente: str
    tipo_de_identificacion_cliente: str
    nombre_cliente: str    
    direccion_cliente: str
    correo_electronico_cliente:str
    telefono_cliente: str