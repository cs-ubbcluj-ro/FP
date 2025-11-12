"""
    -= Procedural programming =-

    Write a console-driven, menu-based application for a library management system. The program's job is to manage
    the library's book database. Each book has a unique title, at least one author and a publishing year.
    The application has the following requirements:

    -= Functional requirements =-
    1. Add a new book (possible only if another book with the same title does not exist)
    2. Remove a book (only if it exists)
    4. Display all books with all their information
    5. Display currently loaned books
    6. Search for a book using partial string matching
    7. Exit the program

    -= Non-functional requirements =-
    - The program must not crash regardless of user input
    - Each menu item links to running a command. The menu is a Python dict of { option : function } mappings
    - Console operations and program logic are kept separate
    - Functions communicate using function arguments, return values and raising exceptions; program logic functions
    have specifications and unit tests (use the assert keyword)
    - The main menu and book lists will be pretty printed :) (use the texttable module)
"""

# hover over texttable -> PyCharm should give you the option of installing the package automatically
from texttable import Texttable

"""
    Program logic (functions that implement requirements, we are not allowed to print/input anything here, we are not 
    allowed to call functions that print/input here either :( )
"""


# Book entity
def create_book(title: str, authors: list[str], year: int):
    """
    Create a book with the given title, list of authors (as string) and publishing year
    Raises ValueError if empty title, no authors or if the publishing year is not in [1000, 2026]
    """
    if title is None or len(title) == 0:
        raise ValueError("Book must have a title!")
    if len(authors) == 0 or len(authors[0]) == 0:
        raise ValueError("Book must have at least one author!")
    if not (1_000 <= year <= 2_026):
        raise ValueError("Book must be published in (1000, 2026)!")
    return {"title": title, "authors": authors, "year": year}


def get_title_book(book) -> str:
    return book["title"]


def get_authors_book(book) -> list[str]:
    """
    Return the list of the book's authors
    """
    return book["authors"]


def get_year_book(book) -> int:
    return book["year"]


def test_book():
    b = create_book("1984", ["George Orwell"], 1949)
    assert "1984" == get_title_book(b)
    assert 1949 == get_year_book(b)
    assert len(get_authors_book(b)) == 1
    assert "George Orwell" == get_authors_book(b)[0]


test_book()

"""
    User interface (all input/prints are done here); functions from UI section call functions from program logic
"""


def add_book_ui(book_list: list) -> None:
    """
    Function to add a new book to the list.
    Raises ValueError in case the title of the new book already exists or in case the book cannot be created

    How to implement:
        1. Read book title
        2. In case the title already exists => raise ValueError with an error message
        3. If the title is unique, read the list of authors (at least one), and the publication year
        4. Create the book (use the create_book function)
        5. Add the book to the list of books
    """
    pass


def remove_book_ui(book_list: list) -> None:
    """
    How to implement:
        1. Update the way books are displayed so that the first column of the table is an index starting at 1
        2. Display the list of all books :) (call the existing function to display a book)
        3. Ask the user the index of the book they want to delete
        4. If the user enters an invalid index (you have 3 books but they enter 4 -> display error message)
        5. If index is valid, delete the book from the list, return to main menu
    """
    pass


def display_books_ui(book_list: list) -> None:
    t = Texttable()  # initialize an empty table
    t.header(["Title", "Author(s)", "Year"])
    for book in book_list:

        # process the authors' list
        authors_str = ""
        for author in get_authors_book(book):
            authors_str += author
            authors_str += ", "
        # FIXME inefficient because it creates a copy of the original string :(
        authors_str = authors_str[:-2]  # remove the final two characters

        # add each book as a separate row in the table
        t.add_row([get_title_book(book), authors_str, get_year_book(book)])
    # draw turns the table into a string
    print(t.draw())


def print_menu():
    print("1. Display all books")
    print("X. Exit")


def start():
    book_list = [create_book("1984", ["George Orwell"], 1949), create_book("Dune", ["Frank Herbert"], 1949),
                 create_book("Geometry 101", ["Pitagora", "Janos Bolyai"], 1849)]
    commands = {"1": display_books_ui}

    while True:
        print_menu()
        opt = input(">")
        if opt in commands:  # is the user's option a valid command?
            # if it is, run it
            # commands -- is a Python dict
            # commands[opt] -- is a reference to a Python function
            # commands[opt](book_list) -- is a Python function call, remember that () is the call operator
            commands[opt](book_list)
        elif opt == "x":
            print("Bye")
            return
        else:
            print("Bad command or file name :)")


start()
