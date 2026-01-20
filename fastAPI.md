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
    if __name__ == "__main__:
        import uvicorn

    # metodo run / arquivo e nome  /    host do /
    #   da lib   /       da api    /   server   /   porta       /   tipo    /   funçao de
    #      |     /(app = FastAPI())/ /          /   do server   /   de logs /   reload
    #      |            |           |               |               |               |
        #  V            V           V               V               V               V    
        uvicorn.run("main:app", host="0.0.0.0", port="8000", log_level="info", reload=True)
```