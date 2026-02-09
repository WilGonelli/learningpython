from sqlalchemy import create_engine # Importa a função create_engine do SQLAlchemy para criar a conexão com o banco
from sqlalchemy.orm import sessionmaker, declarative_base # Importa sessionmaker para criar sessões e declarative_base para modelos ORM

# URL de conexão utilizando pymysql
DATABASE_URL = "mysql+pymysql://root:admin@localhost/Mounthly_bills" # Define a string de conexão com o banco de dados MySQL usando o driver pymysql

# Criação da engine
engine = create_engine( # Cria a engine do SQLAlchemy
    DATABASE_URL, # Passa a URL do banco de dados configurada
    echo=True # Habilita o log de SQL gerado pelo SQLAlchemy (útil para debug)
)

# Configuração da Sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Configura a fábrica de sessões, desabilitando commit/flush automáticos e ligando à engine

# Base para os modelos
Base = declarative_base() # Cria a classe base declarativa da qual os modelos ORM herdarão

# Função para obter a sessão (útil para injeção de dependência no FastAPI)
def get_db(): # Define uma função geradora para obter uma sessão do banco de dados
    db = SessionLocal() # Cria uma nova sessão local
    try: # Inicia um bloco try para garantir o fechamento da sessão
        yield db # Retorna a sessão para ser usada (yield permite que a função seja um gerador)
    finally: # Bloco executado sempre, independente de erro ou sucesso
        db.close() # Fecha a sessão do banco de dados para liberar recursos