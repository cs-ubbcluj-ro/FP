"""
Functions that have to do with the game board
"""
from texttable import Texttable


def create_board() -> list:
    """
    Create the (initially empty) game board. We represent the board as a 3x3 matrix (one Python list
    that has 3 sub-lists of length 3 each).

    How to represent things on the board:
        -1 -> empty square
         0 -> 'O'
         1 -> 'X'
    """
    pass


def get_value_on_board(board: list, row: int, col: int) -> int:
    """
    Return the value on the board at (row, col) coordinates
    :param board:
    :param row:
    :param col:
    :return: -1 if its an empty square, 0 if it's an 'O' and 1 if it's an 'X'
    """
    pass


def move_board(board: list, symbol: str, row: int, col: int):
    """
    Record a move on the board
    :param board: the game board
    :param symbol: One of 'X' (human player), or 'O' (computer player)
    :param row: The row, one of 0, 1 or 2
    :param col: The column, one of 0, 1 or 2
    :return: None
    :raises ValueError if:
        - move would be outside of the board
        - symbol is not one of 'X' or 'O'
        - the (row, col) position already has a symbol on it
    """
    pass


def is_full_board(board: list) -> bool:
    """
    Check whether the game board is full
    :param board: the board
    :return: True if the board is full, False otherwise
    """
    pass


def is_board_won(board: list) -> bool:
    """
    Check whether the game board is won by either player
    :param board: the board
    :return: True if the board is won, False otherwise
    """
    pass


def to_str(board: list) -> str:
    """
    Return the string representation of the board. Use the texttable component to pretty print it
    :param board: The game board
    """
    pass


if __name__ == "__main__":
    t = Texttable()
    t.add_row([' ', 'O', ' '])
    t.add_row([' ', 'X', ' '])
    t.add_row([' ', ' ', 'X'])
    print(t.draw())
