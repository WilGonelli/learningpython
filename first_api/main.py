# importação da lib fastapi
# https://fastapi.tiangolo.com/pt/tutorial/
#                  classe da | função para impor
#                   fastapi  |  condiçoes para a variavel
#                       |    |        |
#                       V    |        V
from fastapi import FastAPI,        Query,                      Body,           Request,        Depends, Header, HTTPException

# importação da lib pydantic - biblioteca para validação de tipos
# esse biblioteca valida os dados e caso seja necessario tenta converter lançando um erro caso ocorra
# https://docs.pydantic.dev/latest/#pydantic-examples
from pydantic import BaseModel

# importação da lib para validação de tipo
from typing import Annotated


import time

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]



# instancia do fastAPI
app = FastAPI()

# o cors dita quem pode se conectar com a aplicação, ou seja, que local da requisição sera permitido a conexão
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # <-- lista de locals aceito para a conexao
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# o middleware é uma função que é executada antes das funções das rotas
# quando definimos um middleware todas as rotas passam por essa função
# caso seja necessario uma função antes de algumas rotas e não obrigatoriamente em todas, podemos usar dependecies nas rotas
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# dessa forma com dependencies, vocce pode criar middlewares que serao executados apenas nas rotas escolhidas
async def verificar_token(x_token: str = Header()):
    if x_token != "token-secreto":
        raise HTTPException(status_code=400, detail="Token inválido")

@app.get("/protegido", dependencies=[Depends(verificar_token)])
async def rota_protegida():
    return {"msg": "Você tem acesso!"}

@app.get("/publico") # Esta rota NÃO executa a verificação
async def rota_publica():
    return {"msg": "Livre para todos"}



# classe do body esperado pela requisição
# usado o pydantic para a validação dos tipos
# util usar essa lib para receber dicas de manipulação do objeto
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# função do tipo get da requisição na raiz - (endpoint '/')
@app.get('/')
async def test():
    return {"msg" : "teste ok"}

# função do tipo get da requisição passando parametros - (endpoint '/items-com-parametros/{item_id}')
# {item_id} = parametro passado na url da requisição
# ex.: http://localhost:8000//items-com-parametros/123456
@app.get("/items-com-parametros/{item_id}") # <-- define a rota
async def read_user_item(   # <-- define a função executada quando acontece a chamada na rota
    item_id: str, needy: str, skip: int = 0, limit: int | None = None   # <-- define os parametros recebidos na rota
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item # <-- define o retorno da requisição na rota

# função do tipo post onde recebe os parametros no body (normalmente um JSON | DICT)
@app.post("/items-com-body/")
async def create_item(item: Item):  # <-- define o parametro usando a classe criada anteriormente
    return item

@app.post("/items-com-body-2/")
async def create_item2(item: Item):
    item_dict = item.model_dump() # <-- converte o body recebido em DICT para facilitar a manipulação
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# é possivel mesclar todos tipos de parametros
# pode se possuir parametros na url, no body e parametro de filtro
@app.put("/items/{item_id}") # <-- recebe o paramtro da requisição da url
async def update_item(item_id: int, item: Item, q: str | None = None):  # <-- recebe o body e o parametro de filtro
# pode-se usar expressao rugular para definir uma validação ex.: pattern="^fixedquery$" <-- isso significa que so pode reeber esse valor
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items3/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None): # <-- validação do tipo e tamanho da variavel 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items4/")
async def read_items(q: Annotated[list[str] | None, Query()] = None): # <-- podemos receber listas como parametros
    print(q)
    query_items = {"q": q}
    return query_items

# Você pode adicionar mais informações sobre o parâmetro.
# Essas informações serão incluídas no OpenAPI gerado e usadas pelas interfaces de documentação e por ferramentas externas.
@app.get("/items5/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",  # <-- informação do parametro
            description="Query string for the items to search in the database that have a good match",  # <-- informação do parametro
            min_length=3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.put("/items6/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        # podemos adicionar exemplo do que esperamos na requisição para ser apresentado no docs
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items7/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        # podemos ter mais de um exemplo assim como exemplos de requisição certa e errada
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3005, log_level="info", reload=True)