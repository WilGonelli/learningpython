import datetime
from pydantic import BaseModel

# Schema base com campos comuns para ler e criar
class BillBase(BaseModel):
    name: str
    estimated_value: str
    initial_mounth: int
    final_mounth: int

# Schema para leitura (o que a API retorna, inclui o ID do banco)
class Bill(BillBase):
    id: int

# schema para leitura dos meses
class Mounth(BaseModel):
    id: int
    name: str

# schema para criar as instancias das contas
class BillInstances(BaseModel):
    mounth_id: int
    bill_id: int
    paid: bool
    real_value: int | None
    paid_date: datetime

