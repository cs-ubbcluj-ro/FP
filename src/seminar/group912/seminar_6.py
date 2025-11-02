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
    - Each menu item links to running a command. The menu is a Python dict of { option : function } mappings
    - Console operations and program logic are kept separate
    - Functions communicate using function arguments, return values and raising exceptions; program logic functions
    have specifications and unit tests (use the assert keyword)
    - The main menu and book lists will be pretty printed :) (use the texttable module)
"""
