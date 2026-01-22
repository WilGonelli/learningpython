from fastapi import FastAPI

from  api.v1 import books

app = FastAPI(
    title="Books catalog",
    description="This API is for saving book information."
)

app.include_router(books.router, prefix="/api/v1/books", tags=["books"])

@app.get('/')
async def root():
    return {"msg":"welcome the book catalog"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3005, log_level="info", reload=True)