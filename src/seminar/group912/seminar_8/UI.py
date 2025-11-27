from texttable import Texttable

from seminar.group912.seminar_8.game import Game


class UI:
    def __init__(self):
        # start up a new game
        self._game = Game()

    def start(self):
        """
        Display the empty board
        Play the game

        Catch FullBoardException and GameWonException and treat them accordingly

        :return:
        """

        # This should print out the board using the Board class __str__
        print(self._game.get_board())

        pass


if __name__ == "__main__":
    # print("Example for what the board should look like")
    # table = Texttable()
    # table.add_row([' ', ' ', ' '])
    # table.add_row([' ', 'X', ' '])
    # table.add_row([' ', ' ', 'O'])
    # print(table.draw())

    ui = UI()
    ui.start()  # starts the game
