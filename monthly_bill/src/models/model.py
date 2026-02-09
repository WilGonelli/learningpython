from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date # Importa tipos de colunas e construtores do SQLAlchemy
from sqlalchemy.orm import relationship # Importa relationship para definir relacionamentos entre tabelas
from config.db import Base # Importa a Base declarativa configurada em config.db

class Bill(Base): # Define a classe Bill herdando de Base, mapeando para uma tabela
    __tablename__ = 'bill' # Define o nome da tabela no banco de dados como 'bill'

    id = Column(Integer, primary_key=True, autoincrement=True) # Define a coluna 'id' como Inteiro, chave primária e autoincremento
    name = Column(String(255), nullable=False) # Define a coluna 'name' como String de até 255 caracteres, não nula
    estimated_value = Column(Integer, nullable=False) # Define a coluna 'estimated_value' como Inteiro, não nula
    initial_date = Column(Date, nullable=False) # Define a coluna 'initial_date' como Data, não nula
    final_date = Column(Date, nullable=False) # Define a coluna 'final_date' como Data, não nula

    # Relacionamento com as instâncias de contas
    instances = relationship("BillInstance", back_populates="bill", cascade="all, delete-orphan") # Define o relacionamento com BillInstance, com exclusão em cascata


class BillInstance(Base): # Define a classe BillInstance herdando de Base
    __tablename__ = 'bill_instance' # Define o nome da tabela no banco de dados como 'bill_instance'

    id = Column(Integer, primary_key=True, autoincrement=True) # Define a coluna 'id' como Inteiro, chave primária e autoincremento
    bill_id = Column(Integer, ForeignKey('bill.id'), nullable=False) # Define a chave estrangeira 'bill_id' referenciando 'bill.id', não nula
    month_year = Column(Date, nullable=False) # Define a coluna 'month_year' como Data, não nula
    paid = Column(Boolean, nullable=False, default=False) # Define a coluna 'paid' como Booleano, não nula, padrão Falso
    real_value = Column(Integer, nullable=True) # Define a coluna 'real_value' como Inteiro, permitindo nulo
    paid_date = Column(Date, nullable=True) # Define a coluna 'paid_date' como Data, permitindo nulo

    # Relacionamentos inversos
    bill = relationship("Bill", back_populates="instances") # Define o relacionamento inverso com a classe Bill
