# Documentação de Arquitetura

## Visão Geral

O projeto utiliza uma **Arquitetura em Camadas** (Layered Architecture) simplificada, comum em microsserviços e APIs construídas com FastAPI. O objetivo é desacoplar a definição da API (rotas), a lógica de negócios e a persistência de dados.

## Componentes Arquiteturais

### 1. Camada de Apresentação (API / Routers)
- **Localização:** `app/api/v1/books.py`
- **Responsabilidade:** 
  - Definir os endpoints HTTP (GET, POST, PUT, DELETE).
  - Receber requisições e validar tipos básicos via Pydantic.
  - Chamar a camada de serviço apropriada.
  - Retornar respostas HTTP adequadas (códigos de status e JSON).

### 2. Camada de Domínio/Schemas (DTOs)
- **Localização:** `app/schemas/book.py`
- **Responsabilidade:**
  - Definir a estrutura dos dados (Data Transfer Objects).
  - Validação de entrada e saída utilizando **Pydantic**.
  - Garante que os dados trafegados estejam no formato correto antes de atingir a lógica de negócio.

### 3. Camada de Serviço (Business Logic)
- **Localização:** `app/services/book_service.py`
- **Responsabilidade:**
  - Contém a lógica de negócio da aplicação.
  - Orquestra as operações, chamando a persistência.
  - Realiza transformações de dados (ex: converter Modelos Pydantic para dicionários).
  - *Nota:* Atualmente implementa filtragem e lógica de atualização.

### 4. Camada de Persistência (Data Access)
- **Localização:** `app/database.py`
- **Responsabilidade:**
  - Abstrair o acesso aos dados.
  - Ler e escrever no arquivo físico `books.json`.
  - *Nota:* Em um cenário real, esta camada conectaria a um banco de dados SQL (via SQLAlchemy/SQLModel) ou NoSQL.

## Fluxo de Dados (Exemplo: Criação de Livro)

1.  **Client** envia `POST /api/v1/books/` com JSON.
2.  **FastAPI** valida o JSON contra o schema `Book`.
3.  **Router** (`api/v1/books.py`) recebe o objeto `Book` e chama `book_service.post_books()`.
4.  **Service** (`services/book_service.py`):
    - Recupera lista atual de livros.
    - Converte o objeto `Book` para dicionário (`model_dump`).
    - Adiciona à lista.
    - Chama `database.save_books()`.
5.  **Database** (`database.py`) serializa a lista e escreve no arquivo `books.json`.

