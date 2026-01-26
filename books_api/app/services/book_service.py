from fastapi import HTTPException, status, Depends
from database import JSONDatabase, get_db
from schemas import book

class BookService:
    """
    Service Layer: This is where the 'Business Logic' lives.
    Separating logic from routes makes the code reusable and cleaner.
    """
    def __init__(self, db: JSONDatabase):
        # We receive the database instance via the constructor (Dependency Injection).
        self.db = db
    
    async def get_books(self, filter_query: str | None):
        """Logic to fetch and filter books."""
        try:
            books = self.db.get_all()
            if filter_query is not None:
                # List comprehension for efficient filtering
                books = [book for book in books if filter_query.lower() in book["title"].lower()]
            return books
        except Exception as e:
            # HTTPException: The standard way to return errors in FastAPI.
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while retrieving books: {str(e)}"
            )

    async def post_books(self, book_item: book.Book):
        """Logic to validate and save a new book."""
        try:
            books = await self.get_books(None)
            # Check for duplicates (Business Rule)
            if any(b["title"] == book_item.title for b in books):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"A book with title '{book_item.title}' already exists."
                )
                
            books.append(book_item.model_dump())
            self.db.save_all(books)
            return {"message": "Book created successfully"}
        except HTTPException:
            raise # Re-raise known errors to be handled by FastAPI
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while saving the book: {str(e)}"
            )
        
    async def update_book(self, title: str, book_data: book.Book):
        """Logic to update a book's information."""
        try:
            books = await self.get_books(None)
            found = False
            book_dict = book_data.model_dump()
            
            for b in books:
                if b["title"] == title:
                    # .update() updates the dictionary with new values
                    b.update(book_dict)
                    found = True
                    break
            
            if not found:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Book with title '{title}' not found."
                )

            self.db.save_all(books)
            return {"message": "Book updated successfully"}
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while updating the book: {str(e)}"
            )

    async def delete_book(self, title: str):
        """Logic to remove a book from the list."""
        try:
            books = await self.get_books(None)
            initial_count = len(books)
            # Filter OUT the book with the matching title
            books = [b for b in books if b["title"] != title]
            
            if len(books) == initial_count:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Book with title '{title}' not found."
                )
                
            self.db.save_all(books)
            return {"message": "Book deleted successfully"}
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while deleting the book: {str(e)}"
            )

def get_book_service(db: JSONDatabase = Depends(get_db)) -> BookService:
    """
    Factory function for the service.
    FastAPI calls this to 'inject' the service into the routers.
    """
    return BookService(db)
    
