from datetime import datetime
from pydantic import BaseModel

class FacturaInDB(BaseModel):
    numero_factura: int=0
    cliente_nombre: str
    numero_identificacion_cliente: str
    direccion_cliente : str
    cod_prod: str
    nomb_articulo: str
    cantidad_art: float
    precio_art: float
    total_arti: float=0
    base_fact:float=0
    iva:float=0
    total_fact: float=0

database_factura = []
generator = {"numero_factura":0}

    

def save_factura(factura_in_db: FacturaInDB):
    generator["numero_factura"] = generator["numero_factura"] + 1
    factura_in_db.numero_factura = generator["numero_factura"]
    database_factura.append(factura_in_db)
    return factura_in_db






