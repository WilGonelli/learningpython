# Books API

Uma API RESTful simples para gerenciamento de um catálogo de livros, construída com Python e FastAPI.

## Estrutura do Projeto

O projeto segue uma arquitetura em camadas para separar responsabilidades:

```
books_api/
├── app/
│   ├── api/          # Controladores da API (Rotas)
│   ├── schemas/      # Modelos Pydantic (Validação de dados)
│   ├── services/     # Regras de negócio
│   ├── database.py   # Camada de persistência (Arquivo JSON)
│   └── main.py       # Ponto de entrada da aplicação
├── requirements.txt  # Dependências do projeto
└── ...
```

## Pré-requisitos

- Python 3.10+
- Virtualenv (recomendado)

## Instalação

1.  Clone o repositório ou navegue até a pasta do projeto.
2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Linux/Mac
    source .venv/bin/activate
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento:

```bash
python app/main.py
```
Ou diretamente via uvicorn (executando da raiz):
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 3005
```

A API estará disponível em: `http://localhost:3005`

## Documentação Interativa

O FastAPI fornece documentação automática:
- Swagger UI: `http://localhost:3005/docs`
- ReDoc: `http://localhost:3005/redoc`

## Funcionalidades

- **Listar Livros**: `GET /api/v1/books/` (suporta filtro por título)
- **Adicionar Livro**: `POST /api/v1/books/`
- **Atualizar Livro**: `PUT /api/v1/books/{title}`
- **Remover Livro**: `DELETE /api/v1/books/{title}`
