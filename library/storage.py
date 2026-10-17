import os 
import json

from library.book import Book

DATA_FOLDER = "data"
DATA_FILE = "books.json"
# named at the top so nobody look for it. 

class JsonStorage:
    def __init__ (self,folder:str=DATA_FOLDER, filename: str = DATA_FILE):
        self.folder = folder 
        self.path =  os.path.join(folder, filename)
        #os.path.join instead of folder + "/" filename
        # Heads up : windows uses \ so we shouldn't care which machine we are on.

    def _ensure_folder(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        # Crete data/ the first time.

    def load(self) -> list:
        if not os.path.exists(self.path):
            return[]
        # no file yet just means an empty library.

        try : 
            with open(self.path, "r", encoding="utf-8") as file:
                raw = json.load(file)
                # with closess the file even if an error occurs.
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in storage file.")

        except OSError :
            raise ValueError("Error reading storage file.")
        # OSError covers permission problems, a miising disk,memory,locked file and etc.

        if not isinstance(raw,list):
            raise ValueError("Storage file must contain a list of books.")
        # the file could hold anything, so check the shape before. 

        books = []
        for item in raw :
            books.append(Book.from_dict(item))
        return books
        # we return Book objc, NEVER RAW DICTS.
    

    def save(self,books: list):
        self._ensure_folder()
        # make sure data/ exists.

        data = []
        for book in books:
            data.append(book.to_dict())

        try:
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                # "ensure_ascii = False" --> keeps Farsi/Persian text readeable.
        except OSError:
            raise ValueError("Error writing to storage file.")