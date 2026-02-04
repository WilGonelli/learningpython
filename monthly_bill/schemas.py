from pydantic import BaseModel
from typing import Optional

# Schema base com campos comuns para ler e criar
class BillBase(BaseModel):
    name: str
    description: Optional[str] = None
    amount: float
    is_paid: bool = False

# Schema para criação (o que o usuário manda no POST)
class BillCreate(BillBase):
    pass

# Schema para leitura (o que a API retorna, inclui o ID do banco)
class Bill(BillBase):
    id: int

    class Config:
        # Permite que o Pydantic leia dados de objetos ORM (SQLAlchemy) e não só dicionários
        from_attributes = True
