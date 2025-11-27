class BoardWonException(Exception):
    """
    Raise this when the board is won
    """
    pass


class BoardFullException(Exception):
    """
    Raise this when the board is full
    """
    pass


class Board:
    """
    Class names start with uppercase
        ex: PetrolCar, JetEngine, Student

    An object of the Board class represents the board the game is played on
    """

    def __init__(self):
        """
        Create the game board

        Board cells:
        0  - Empty cell
        1  - 'X' played
        -1 - 'O' played
        """
        self._data = [0] * 9
        # print(self._data, type(self._data))

    def _is_won(self):
        """
        Return True if and only if the board is won. Called from the move() method
        :return:
        """
        pass

    def _is_full(self):
        """
        Return True if and only if the board is full. Called from the move() method
        :return:
        """
        pass

    def get_cell(self, row: int, col: int):
        """
        Returns the state of the cell at (row,col) on the board
        Board cell states:
             0 - Empty cell
             1 - 'X' played
            -1 - 'O' played

        :param board: The game board
        :param row: Row
        :param col: Column
        """
        pass

    def move(self, symbol: str, row: int, col: int):
        """
        Record a new move on the board. Internally calls the _is_full() and
        _is_won() methods to check the board

        :param symbol: One of 'X' or 'O'
        :param row: Must be one of 0, 1 or 2
        :param col: Must be one of 0, 1 or 2

        :raises ValueError if the move is outside the board, the symbol
        placed is invalid or the [row,col] is already taken by another
        symbol

        :raises BoardWonException if the board is won
        :raises BoardFullException if the board is full, but not won
        """
        pass

    def __str__(self):
        """
        Return the board's representation as a Python str, using the texttable
        module.

        >>> from texttable import Texttable

        NB! Texttable is a class :)

        :return:
        """
        pass


if __name__ == "__main__":
    b = Board()  # calls the class constructor => __init__
    print(b)  # this should print the empty board

    b.move('X', 1, 1)  # play X in the center
    b.move('O', 0, 0)
    b.move('X', 0, 1)
    b.move('O', 2, 2)
    try:
        # this move should win the game
        b.move('X', 2, 1)
    except BoardWonException as be:
        print(be)
        print(b)
