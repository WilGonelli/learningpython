# Biblioteca SQLAlchemy

O SQLAlchemy é uma biblioteca ORM (Object Relational Mapper)

#### como usar

normalmente voce cria um arquivo chamado models.py onde dentro voce tera as classes que é a declaração da tabela

* ex.:
```python
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

#

### conexao com db

* usa uma string de conexao unica

```python
    engine = create_engine(url='postgres://user:pass@ip:port/database')
    engine = create_engine(url='postgres://root:admin@localhost:5432/my_database')
```

dessa forma fica mais facil a alteração do db utilizado

* ex. de configuração

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexão (exemplo com MySQL + PyMySQL)
DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/Mounthly_bills"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True mostra os SQLs gerados
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
```

* ex. de modelo de tabela

```python
class Bill(Base):
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    estimated_value = Column(Integer)
    initial_mounth = Column(Integer)
    final_mounth = Column(Integer)

```

ex. CRUD basico

```python
def insert_bill():
    session = SessionLocal()
    new_bill = Bill(
        name="Conta de Luz",
        estimated_value=150,
        initial_mounth=2,
        final_mounth=2
    )
    session.add(new_bill)
    session.commit()   # grava no banco
    session.refresh(new_bill)  # atualiza com o ID gerado
    session.close()
    return new_bill


def select_bills():
    session = SessionLocal()
    bills = session.query(Bill).all()  # SELECT * FROM bill
    session.close()
    return bills

def select_bill_by_id(bill_id):
    session = SessionLocal()
    bill = session.query(Bill).filter(Bill.id == bill_id).first()
    session.close()
    return bill


def update_bill(bill_id, new_value):
    session = SessionLocal()
    bill = session.query(Bill).filter(Bill.id == bill_id).first()
    if bill:
        bill.estimated_value = new_value
        session.commit()
    session.close()
    return bill


def delete_bill(bill_id):
    session = SessionLocal()
    bill = session.query(Bill).filter(Bill.id == bill_id).first()
    if bill:
        session.delete(bill)
        session.commit()
    session.close()
    return bill

```


* relacionamentos entre tabelas

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    # Relacionamento: um usuário pode ter várias contas
    bills = relationship("Bill", back_populates="owner")


class Bill(Base):
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    estimated_value = Column(Integer)

    # Chave estrangeira para User
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relacionamento inverso
    owner = relationship("User", back_populates="bills")



def select_user_with_bills(user_id):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

# Exemplo de uso:
user = select_user_with_bills(1)
print(user.name)
for bill in user.bills:
    print(bill.name, bill.estimated_value)


def delete_bill(bill_id):
    session = SessionLocal()
    bill = session.query(Bill).filter(Bill.id == bill_id).first()
    if bill:
        session.delete(bill)
        session.commit()
    session.close()

```

ex. de relacionamento m to m
```python

from sqlalchemy import Table, Column, Integer, ForeignKey

association_table = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id")),
    Column("course_id", ForeignKey("courses.id"))
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    courses = relationship("Course", secondary=association_table, back_populates="students")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))

    students = relationship("Student", secondary=association_table, back_populates="courses")

```