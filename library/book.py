from dataclasses import dataclass

MAX_TITLE_LENGTH = 100 
MAX_AUTHOR_NAME = 100

@dataclass
# Writes __init__, __repe__ and etc.

class Book :
    title : str 
    author : str 
    read: bool = False
    id : int = 0 
    # Tip : Fileds with def must comes last --> Python requires it 

    def __post_init__(self):
        if not isinstance(self.title, str):
            print("Title must be String")
        if not isinstance(self.author, str):
            print("Author must be String")

        self.title = self.title.strip()
        self.author = self.author.strip()

        if self.title == "":
            raise ValueError("Title cannot be empty")
        if self.author == "":
            raise ValueError("Author cannot be empty")

        if len(self.title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Title cannot exceed {MAX_TITLE_LENGTH} characters")
        if len(self.author) > MAX_AUTHOR_NAME:
            raise ValueError(f"Author name cannot exceed {MAX_AUTHOR_NAME} characters")
    
    def mark_read(self):
        # A method instead of setiing book.rad = True from outside.
        self.read = True

    def mark_unread(self):
        # A method instead of setiing book.rad = False from outside.
        self.read = False

    def to_dict(self):
        # The book knows its own fields, so the book Builds own dict.
        return {
            "title": self.title,
            "author": self.author,
            "read": self.read,
            "id": self.id
        }
    
    @classmethod
    # A classmethod cause building a Book is the Book's Job.
    def from_dict(cls, data: dict) -> "Book":
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")

        for key in ["id", "title", "author", "read"]:
            if key not in data:
                raise ValueError(f"Missing key: {key}")
            #check every required field before touching any of them. 

        return cls(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            read=bool(data.get("read", False))
            #.get with a default value of False in case the key is missing
        )