"""
Handles the board entity for our Tic Tac Toe game
    - not a UI module, so no prints/inputs here :(
    - represent the board using a to_str() method
"""


def create_board():
    """
    Create an empty Tic Tac Toe board. The board is represented as a
    list of lists

    Board cells:
        0 - Empty cell
        1 - 'X' played
        2 = 'O' played

    Function must return an empty board
    """
    pass


def is_won_board(board: list) -> bool:
    """
    Verify whether the board was won by either player
    :rtype: bool True if the board is won, False otherwise
    :param board: The game board

    Check whether the same symbol appears on 3 time on the same row,
    the same column or one of the diagonals
    """
    pass


def is_full_board(board: list) -> bool:
    """
    Verify whether the board is full
    :rtype: bool True if board is full, False otherwise
    :param board:
    """
    pass


def move_board(board: list, symbol: str, row: int, col: int):
    """
    Record a new move on the board

    :param board: The board itself
    :param symbol: One of 'X' or 'O'
    :param row: Must be one of 0, 1 or 2
    :param col: Must be one of 0, 1 or 2
    :raises ValueError if the move is outside the board, the symbol
    placed is invalid or the [row,col] is already taken by another
    symbol
    """
    pass


def get_cell_board(board: list, row: int, col: int) -> int:
    """
    Returns the state of the cell at (row,col) on the board
    Board cell states:
        0 - Empty cell
        1 - 'X' played
        2 = 'O' played

    :param board: The game board
    :param row: Row
    :param col: Column
    """
    pass


def to_str(board: list) -> str:
    """
    Return the string representation of the board. Use the textable
    module to pretty print the board :) Call this function from the
    UI to display the board ( like print(to_str(board)) )
    :param board:
    """
    pass
