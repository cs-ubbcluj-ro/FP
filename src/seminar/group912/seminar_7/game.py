"""
Handle the human player's and the computer's moves on the board
    - human player -> easy, received from the UI
    - computer player -> make valid moves
"""


def human_move(board, row: int, col: int):
    """
    Record the human player's move on the board. The move coordinates
    are received from the UI. Human player plays with 'X' and always
    makes the game's first move

    :param board: The game board
    :param row: Row to move on
    :param col: Column to move on

    Call the move_board function from the board module with the
    required parameters
    """
    pass


def computer_move(board):
    """
    Calculate and make the computer's move. Computer moves in the first
    empty cell it finds.

    :param board: The game board
    :return: The (row, column) where the computer moved
    """
    pass
