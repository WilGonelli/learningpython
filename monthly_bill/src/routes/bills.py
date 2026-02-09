from datetime import date # Importa a classe date do módulo datetime
from fastapi import APIRouter, Depends, HTTPException, status # Importa utilitários do FastAPI para rotas, injeção de dependência e erros
from sqlalchemy.orm import Session # Importa a classe Session do SQLAlchemy para tipagem
from typing import List # Importa List do módulo typing para dicas de tipo

from config.db import get_db # Importa a função get_db para obter a sessão do banco
from schemas.schemas import BillBase, Bill as BillSchema, BillInstanceSchema # Importa os schemas Pydantic
from services.bill_service import BillService # Importa a classe de serviço BillService

router = APIRouter( # Cria um roteador API
    prefix="/bills", # Define o prefixo da URL para todas as rotas deste roteador como "/bills"
    tags=["bills"] # Define a tag para documentação automática (Swagger UI)
)

# Instanciamos o serviço (ou poderíamos usar injeção de dependência mais complexa)
service = BillService() # Cria uma instância do serviço BillService

@router.post("/", response_model=BillSchema, status_code=status.HTTP_201_CREATED) # Define rota POST na raiz do prefixo, retornando BillSchema e status 201
def create_bill(bill: BillBase, db: Session = Depends(get_db)): # Função para criar conta, recebendo dados da conta e sessão do banco injetada
    """
    Cria uma nova conta.
    """
    return service.create_bill(bill, db) # Chama o serviço para criar a conta passando os dados e a sessão

@router.get("/", response_model=List[BillSchema]) # Define rota GET na raiz, retornando uma lista de BillSchema
def read_bills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)): # Função para ler contas, com parâmetros de paginação e sessão do banco
    """
    Lista todas as contas com paginação.
    """
    return service.get_bills(db, skip=skip, limit=limit) # Chama o serviço para obter a lista de contas

@router.get("/instances", response_model=List[BillInstanceSchema]) # Define rota GET em "/instances", retornando lista de BillInstanceSchema
def read_bills(mounth_ref: date, db: Session = Depends(get_db)): # Função para ler instâncias de um mês específico (Nota: nome da função repetido 'read_bills')
    """
    Lista todas as contas do mes referencia.
    """
    return service.get_instances(db, mounth_ref) # Chama o serviço para obter as instâncias do mês de referência
