from seminar.group912.seminar_8.board import Board


class Game:
    def __init__(self):
        # Creating a new game starts an empty board
        self._board = Board()

    def get_board(self):
        """
        give access to the game board from the UI

        :return:
        """
        return self._board

    def human_move(self, row: int, col: int):
        """
        Record the human player's move on the board. The move coordinates
        are received from the UI. Human player plays with 'X' and always
        makes the game's first move

        Access the board using:
        >>> self._board

        :param board: The game board
        :param row: Row to move on
        :param col: Column to move on

        Call the move() function from the Board class with the
        required parameters
        """
        pass

    def computer_move(self):
        """
        Calculate and make the computer's move. Computer should:
            - win immediately if possible
            - prevent the human from winning on the next move, if possible
            - play in the center, otherwise
            - play randomly, otherwise

        Access the board using:
        >>> self._board
        """
        pass
