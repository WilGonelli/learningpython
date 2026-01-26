import json
from pathlib import Path
from schemas import book

class JSONDatabase:
    """
    Handles persistence logic using a JSON file.
    This can be swapped for a real database implementation in the future.
    """
    def __init__(self, file_path: str = "books.json"):
        self.db_path = Path(file_path)

    def get_all(self) -> list:
        if not self.db_path.exists() or self.db_path.stat().st_size == 0:
            return []
        
        with open(self.db_path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def save_all(self, data: list):
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

# Dependency provider for the database
def get_db() -> JSONDatabase:
    return JSONDatabase()