"""
    -= Procedural programming =-

    Write a console-driven, menu-based application for a library management system. The program's job is to manage
    the library's book database. Each book has a unique title, at least one author and a publishing year.
    The application has the following requirements:

    -= Functional requirements =-
    1. Add a new book (possible only if another book with the same title does not exist)
    2. Mark a book as being on loan / returned
    3. Remove a book (only if it exists and is not currently on loan)
    4. Display all books with all their information
    5. Display currently loaned books
    6. Search for a book using partial string matching
    7. Exit the program

    -= Non-functional requirements =-
    - The program must not crash regardless of user input
    - Each menu item links to running a command. The menu is a Python
    dict of { option : function } mappings
    - Console operations and program logic are kept separate
    - Functions communicate using function arguments, return values
    and raising exceptions; program logic functions
    have specifications and unit tests (use the assert keyword)
    - The main menu and book lists will be pretty printed :)
    (use the texttable module)
"""
from texttable import Texttable

"""
    Program logic goes here
    (no input/print statements are allowed here, none of the function
    defined here may call any functions from the UI :) )
"""


# Book functions go here

def create_book(title: str, authors: list[str], year: int):
    """
    Create a new book with given title, author list and year
    @param: title
    @param: authors
    @param: year
    Return the newly created book
    Raise ValueError if book title is empty, there are no authors
    or year is not between 1000 and 2026
    """
    if title is None or len(title) == 0:
        raise ValueError("Invalid book title")
    if len(authors) == 0 or len(authors[0]) == 0:
        raise ValueError("No authors or invalid 1st author")
    if not (1000 <= year <= 2026):
        raise ValueError("Invalid publication year")
    return {"title": title, "authors": authors, "year": year}


def get_authors_book(book) -> list[str]:
    return book["authors"]


def get_title_book(book) -> str:
    return book["title"]


def get_year_book(book) -> int:
    return book["year"]


def test_book():
    b = create_book("1984", ["George Orwell"], 1949)
    assert get_year_book(b) == 1949
    assert get_title_book(b) == "1984"
    assert len(get_authors_book(b)) == 1
    assert get_authors_book(b)[0] == "George Orwell"


test_book()

# Rest of program logic

"""
    User interface goes here
    (here we catch any Errors that might be raised from program
    logic)
"""


def add_book_ui(book_list: list):
    # 1. Read book title
    # 2. If book already exists => raise ValueError
    # 3. If title is new => read author & book year information
    # 4. Everything ok => add book to list of books
    print("Add a book")


def find_books_ui(book_list: list):
    """
    Search for books by partially matching the title or any of its
    authors
    """

    # 1. Read the search string from the user
    # 2. Go through the list of books and check if search string is
    # included in book title or book author(s)
    # 3. If yes => add the book to a list of book
    # 4. At the end, print out the list using a Texttable
    print("Find a book")


def print_menu():
    """
    1. Display all books
    x. Exit program
    """
    t = Texttable()  # t is a texttable, we have to add rows to it
    t.header(["", "Bookstore menu"])
    t.add_row(["1", "Display all books"])
    t.add_row(["2", "Add new book"])
    t.add_row(["3", "Search for a book"])
    t.add_row(["X", "Exit"])
    print(t.draw())


def display_books_ui(book_list: list):
    t = Texttable()
    t.header(["Title", "Author(s)", "Year"])
    for book in book_list:
        author_str = ""
        for author in get_authors_book(book):
            author_str += author
            author_str += ", "

        author_str = author_str[:-2]
        t.add_row([get_title_book(book), author_str, get_year_book(book)])
    print(t.draw())


def start():
    book_list = [create_book("1984", ["George Orwell"], 1949),
                 create_book("Dune", ["Frank Herbert"], 1956),
                 create_book("Basic Maths", ["Lulea Traian", "Popescu Mariana"], 1970)
                 ]
    commands = {"1": display_books_ui, "2": add_book_ui, "3": find_books_ui}

    while True:
        print_menu()
        option = input(">")
        if option in commands:
            commands[option](book_list)
        elif option == "x":
            return
        else:
            print("Invalid option")


# https://classroom.github.com/a/iF75ai5J
start()
