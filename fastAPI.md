## usando o FastAPI

#### instalando
* rodar o comando:
```bash
    pip install fastapi
```

* instalando uvicorn (servidor)
* rodar o comando:
```bash
    pip install uvicorn
```

#### documentação

* o fastAPI cria uma documentação automatica que pode ser acessado atraves do:
    * http://{ip do servidor}/docs
    * http://{ip do servidor}/redoc

#

#### utils uvicorn

* para executar um projeto usando uvicorn podemos adicionar o seguinte comando ao main do projeto:
```python
    if __name__ == "__main__":
        import uvicorn

    # metodo run / arquivo e nome  /    host do /
    #   da lib   /       da api    /   server   /   porta       /   tipo    /   funçao de
    #      |     /(app = FastAPI())/ /          /   do server   /   de logs /   reload
    #      |            |           |               |               |               |
        #  V            V           V               V               V               V    
        uvicorn.run("main:app", host="0.0.0.0", port="8000", log_level="info", reload=True)
```
#### modelo de estrutura de pastas para api com fastapi

```bash
my_ebook_api/
│
├── app/
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── models/              # Modelos de dados (ORM)
│   │   └── book.py          # Modelo do livro
│   ├── routers/             # Rotas da API
│   │   ├── __init__.py
│   │   └── books.py         # Rotas relacionadas aos livros
│   ├── schemas/             # Schemas de validação (Pydantic)
│   │   └── book.py          # Schema do livro
│   ├── services/            # Lógica de negócio
│   │   └── book_service.py  # Serviços relacionados a livros
│   ├── database/            # Configuração do banco de dados
│   │   └── db.py            # Conexão com o banco de dados
│   ├── utils/               # Funções utilitárias
│   │   └── helpers.py       # Funções auxiliares
│   └── config.py            # Configurações gerais
│
└── requirements.txt          # Dependências do projeto


# clean Architecture
ebook_api/
├── app/
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── api/             # Rotas (Endpoints)
│   │   └── v1/
│   │       └── books.py
│   ├── core/            # Configurações globais (env, segurança)
│   ├── models/          # Modelos do Banco de Dados (SQLAlchemy/SQLModel)
│   ├── schemas/         # Modelos de Validação (Pydantic)
│   ├── services/        # Lógica de negócio (Regras de cadastro, filtros)
│   └── database.py      # Conexão e sessão do banco
├── tests/               # Testes automatizados
├── .env                 # Variáveis de ambiente
└── requirements.txt     # Dependências
```