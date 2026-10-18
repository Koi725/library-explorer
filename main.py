from library.library import Library
from library.storage import JsonStorage

library = Library(JsonStorage())

# MENU ="\n1 add 2 list 3 get 4 count 5 exit\n"

# book = library.add("The Great Gatsby", "F. Scott Fitzgerald")
# library.add("To Kill a Mockingbird", "Harper Lee")


# print(library.all(sort_by="title")) 
# print(library.all())
# print(library.count())
# print(library.is_empty())
# print(library.get(book.id))


# while True:
#     print(MENU)
#     choice = input("> ").strip()

#     try:
#         if choice == "1":
#             title = input("Title: ")
#             author = input("Author: ")
#             book = library.add(title, author)
#             print(f"Added book with ID {book.id}")

#         elif choice == "2":
#             books = library.all(sort_by="title")
#             for book in books:
#                 print(f"{book.id}: {book.title} by {book.author}")

#         elif choice == "3":
#             book_id = input("Book ID: ")
#             book = library.get(book_id)
#             if book:
#                 print(f"{book.id}: {book.title} by {book.author}")

#         elif choice == "4":
#             count = library.count()
#             print(f"Total books: {count}")

#         elif choice == "5":
#             print("Exiting...")
#             break

#         else:
#             print("Invalid choice. Please try again.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


def show_menu():
    # print the numbered options so the user knows what they can type
    pass


def print_book():
    # take one book and print it as a single readable line
    pass


def print_books():
    # take a list of books and print each one, or say so when the list is empty
    pass


def ask_text():
    # ask the user a question and give back their answer with spaces trimmed
    pass


def ask_number():
    # ask for a number and give back None instead of crashing when it is not one
    pass


def do_list():
    # ask how to sort, then print every book in that order
    pass


def do_search_list():
    # ask for a word and print only the books whose title or author contain it
    pass


def do_mark_read():
    # ask for an id and tell the library to mark that book as read
    pass


def do_mark_unread():
    # ask for an id and tell the library to mark that book as not read again
    pass


def do_unread():
    # print only the books that have not been read yet
    pass


def do_delete():
    # ask for an id, confirm with the user, then remove that book for good
    pass


def main():
    # create the library, then loop: show the menu, read the choice, call the right function
    pass


main()