from fastapi import FastAPI

api = FastAPI()

@api.get('/')
async def test():
    return {"msg" : "teste ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:api", host="0.0.0.0", port=3005, log_level="info", reload=True)