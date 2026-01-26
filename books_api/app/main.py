from fastapi import FastAPI
from api.v1 import books

# FastAPI instance: This is the main object of your application.
# It handles all the configuration, documentation, and routing.
app = FastAPI(
    title="Books catalog",
    description="This API is for saving book information.",
    version="1.0.0"
)

# app.include_router: This is how we modularize the application.
# Instead of putting all routes here, we group them in other files (routers).
# prefix: All routes inside 'books.router' will start with /api/v1/books
# tags: Used for grouping routes in the automatic documentation (/docs)
app.include_router(books.router, prefix="/api/v1/books", tags=["books"])

@app.get('/')
async def root():
    """
    Root endpoint: A simple welcome message.
    'async def' tells FastAPI that this function can run asynchronously.
    """
    return {"msg": "Welcome to the book catalog"}


if __name__ == "__main__":
    # uvicorn: The ASGI server that actually runs the FastAPI code.
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3005, log_level="info", reload=True)