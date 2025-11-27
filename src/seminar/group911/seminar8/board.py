from texttable import Texttable


class BoardFullException(Exception):
    """
    This is a Python Exception (we know, because it's inherited from the Exception
    class => it can be raised and caught

    If you want, you can create it using a message:
    >>> raise BoardFullException("The board is full")

    An explicit constructor is not reqiured here, as the Exception class already
    has one that can be called implicitly
    """
    pass


class BoardWonException(Exception):
    pass


class Board:
    """
    Each object of this class represents a game board for Tic Tac Toe
    """

    def __init__(self):
        """
        This method is called by the Python interpreter when creating a new Board

        How do we represent data on the board?
        0  - empty cell
        1  - X
        -1 - O
        """
        self._data = [0] * 9  # a list of 9 elements, each equal to 0
        self._move_counter = 0  # increase by 1 after each successful move

    def _is_won(self):
        """
        Check whether the board was won
        This method is private, as we don't want it to be called from outside the
        class

        0 1 2
        3 4 5
        6 7 8

        Hint:
        Check win on a row
        # in a for loop
        >>> abs(sum(self._data[0:3])) == 3 # checks for row for a win
        # FIXME !?
        >>> any(abs(sum(self._data[i:i+3])) == 3 for i in (0,3,6))

        Check win on a column
        >>> self._data[0::3] # checks first column

        :return: Return True if and only if board was won
        """
        pass

    def _is_full(self):
        """
        Check whether the board is full

        Hint: Count the moves

        :return:
        """
        return self._move_counter == 9

    def get_value(self, row: int, col: int) -> int:
        """
        Return the state of the (row, col) cell

        :param row:
        :param col:
        :return: 0 if empty cell, 1 if X, -1 if O
        """
        pass

    def move(self, symbol: str, row: int, col: int):
        """
        Record a move on the board
        :param symbol: One of 'X' (human player), or 'O' (computer player)
        :param row: The row, one of 0, 1 or 2
        :param col: The column, one of 0, 1 or 2
        :return: None

        :raises ValueError if:
            - move would be outside of the board
            - symbol is not one of 'X' or 'O'
            - the (row, col) position already has a symbol on it

        :raises BoardFullException if:
            - The board is full after this move, but the board was not won

        :raises BoardWonException if:
            - The board is won after this move
        """
        self._move_counter += 1
        pass

    def __str__(self):
        """
        Return the string representation of the board.
        Use the texttable component to pretty print it

        example:
        >>> from texttable import Texttable

        --> Texttable is a class

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
