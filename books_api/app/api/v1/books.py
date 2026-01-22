from fastapi import APIRouter

from  schemas import book

router = APIRouter()

@router.get("/", response_model=list[book.Book] | None)
async def get_books():
    print("ok get")
    return None

@router.post("/", response_model=book.Book | None)
async def post_book(book: book.Book):
    print(book)
    print("ok post")
    return None