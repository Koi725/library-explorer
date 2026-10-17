from library.book import Book

SORT_FIELDS = ["id", "title", "author", "read"]

class Library:
    def __init__(self,storage):
        self._storage = storage
        # We Receive storage form ouside instead of building it that's what lets us swap JsonStorage.
        self._books = self._storage.load()
        # The underscore means "internal, don't teouch from outside"

    def count (self) -> int :
        return len(self._books)

    def is_empty(self) -> bool:
        return len(self._books) == 0

    def _next_id(self) -> int :
        biggest = 0 
        for book in self._books:
            if book.id > biggest:
                biggest = book.id
        return biggest + 1

    def has_title(self, title:str) -> bool:
        title = title.strip().lower()
        for book in self._books:
            if book.title.lower() == title:
                return True
        return False
    # So we can warn aboiut duplicated before adding a new book.

    def add(self, title:str, author:str) -> Book:
        if self.has_title(title):
            raise ValueError("Book with this title already exists.")
        book = Book(title=title, author=author, id=self._next_id())
        self._books.append(book)
        self._storage.save(self._books)
        return book
    # We return new book so the user can see which id it  got.
    # returning nothing would make users them search for what they just created 

    def get (self, book_id:int) -> Book:
        for book in self._books:
            if book.id == book_id:
                return book
        raise ValueError("Book not found.")



    def all(self, sort_by: str = "id", reverse : bool = False) -> list:
        books = self._books[:]
        # [:] makes a copy of the list.

        if sort_by not in SORT_FIELDS:
            sort_by = "id"
            # an unknown sort field falls back to id.

        if sort_by == "title" :
            books.sort(key=lambda book: book.title.lower(), reverse=reverse)
            # Heads Up : .lower() in the key so "apple" and "Apple" sort together.
            # Tip : without .lower() Captial letteres comes first so sort feel like random.
        elif sort_by == "author":
            books.sort(key=lambda book: book.author.lower(), reverse=reverse)
        elif sort_by == "read":
            books.sort(key=lambda book: book.read, reverse=reverse)
        else:
            books.sort(key=lambda book: book.id, reverse=reverse)
        return books
        # Sorting happen on the copy, so the stored order is never touched.
    
    
    def delete():
        # find the book by id, remove it from the list, and save the file
        pass

    def search():
        # return every book whose title or author contains the given word
        pass

    def edit():
        # find the book by id, replace its title or author, and save the file
        pass

    def read():
        # find the book by id, mark it as read, and save the file
        pass

    def unread():
        # find the book by id, mark it as not read, and save the file
        pass