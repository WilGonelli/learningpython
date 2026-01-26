from fastapi import APIRouter, status, Depends
from schemas import book
from services.book_service import BookService, get_book_service

# APIRouter: A mini FastAPI instance used only for specific modules (like books).
router = APIRouter()

@router.get("/", response_model=list[book.Book])
async def get_books(
    filter_query: str | None = None,
    # Depends: This is FastAPI's Dependency Injection. 
    # It says: "Before running this function, call get_book_service() and give me the result."
    # This keeps our code clean and easy to test.
    service: BookService = Depends(get_book_service)
):
    """
    List all books with an optional title filter.
    FastAPI automatically converts the JSON result to the 'response_model' format.
    """
    return await service.get_books(filter_query)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_book(
    book_item: book.Book,
    service: BookService = Depends(get_book_service)
):
    """
    Add a new book to the catalog.
    'book_item' is automatically validated by Pydantic. 
    If the JSON is wrong, FastAPI returns a 422 error automatically.
    """
    return await service.post_books(book_item)

@router.put("/{title}")
async def update_book(
    title: str, 
    book_item: book.Book,
    service: BookService = Depends(get_book_service)
):
    """
    Update an existing book by its title.
    {title} in the path is captured as the 'title' parameter.
    """
    return await service.update_book(title, book_item)

@router.delete("/{title}")
async def delete_book(
    title: str,
    service: BookService = Depends(get_book_service)
):
    """
    Remove a book from the catalog.
    """
    return await service.delete_book(title)

