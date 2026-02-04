# Biblioteca SQLAlchemy

O SQLAlchemy é uma biblioteca ORM (Object Relational Mapper)

#### como usar

normalmente voce cria um arquivo chamado models.py onde dentro voce tera as classes que é a declaração da tabela

* ex.:
````python
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    amount_estimated = Column(Integer, nullable=False)
    initial_mounth = Column(Integer, nullable=False)
    final_mounth = Column(Integer, nullable=False)
```

