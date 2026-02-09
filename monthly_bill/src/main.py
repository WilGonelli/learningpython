# from database.database import get_bills # Importação comentada de um módulo de banco de dados antigo ou alternativo
#
# resultado = get_bills() # Chamada comentada da função get_bills
# print(resultado) # Impressão comentada do resultado

from fastapi import FastAPI # Importa a classe FastAPI do framework FastAPI
from routes import bills # Importa o módulo de rotas 'bills'
from config.db import engine, Base # Importa a engine de banco de dados e a Base declarativa do arquivo de configuração
# Cria as tabelas no banco de dados se elas não existirem
# Isso substitui a necessidade de rodar o script SQL manualmente
Base.metadata.create_all(bind=engine) # Cria todas as tabelas definidas nos modelos herdados de Base usando a engine configurada
app = FastAPI(title="Monthly Bill API") # Cria uma instância da aplicação FastAPI com o título "Monthly Bill API"

# Inclui as rotas que criamos
app.include_router(bills.router) # Inclui o roteador definido no módulo 'bills' na aplicação principal

@app.get("/") # Define uma rota para o caminho raiz ("/") usando o método HTTP GET
def home(): # Define a função 'home' que será executada ao acessar a rota raiz
   return {"message": "Monthly Bill API is running"} # Retorna um dicionário JSON com uma mensagem de status

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente (não importado)
        import uvicorn # Importa o servidor ASGI uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True) # Inicia o servidor uvicorn com a aplicação 'app' no host 0.0.0.0 e porta 8000, com reload automático