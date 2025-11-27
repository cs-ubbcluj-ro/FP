from seminar.group911.seminar8.board import Board


class Game:
    def __init__(self):
        self._board = Board()

    def get_board(self):
        """
        Return the board. Will be called from the UI in order to display the board
        on the screen
        :return:
        """
        return self._board

    def move_human(self, row: int, col: int):
        """
        Record the human player's move on the board
        :param board:
        :param row:
        :param col:
        """
        pass

    def move_computer(self):
        """
        Calculate the computer's move and make it. The computer makes random, but valid moves on
        the board.
        :param board: the board

        There should be no exceptions here, because the computer should validate the validity
        of its moves.
        """
        pass
