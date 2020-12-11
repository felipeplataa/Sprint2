from pydantic import BaseModel
from datetime import datetime

class FacturaIn(BaseModel):
    cliente_nombre: str
    numero_identificacion_cliente: str
    direccion_cliente : str
    cod_prod: str
    cantidad_art: float


class FacturaOut(BaseModel):
    numero_factura: int=0
    cliente_nombre: str
    numero_identificacion_cliente: str
    direccion_cliente : str
    fecha_expedicion: datetime = datetime.today() 
    nomb_articulo: str
    cantidad_art: float
    precio_art: float
    total_arti: float
    base_fact:float
    iva:float
    total_fact: float