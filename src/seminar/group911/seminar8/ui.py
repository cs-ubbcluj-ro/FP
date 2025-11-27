from seminar.group911.seminar8.game import Game


class UI:
    def __init__(self):
        self._game = Game()

    def start(self):
        """
        How the UI should work:
            1. Show the (initially empty) game board
                -> we do this by calling to_str() from the board module
            2. Read the human player's move
                -> catch any ValueError and print out its message
                -> repeat reading the move until the move is valid :)
            3. Calculate and make the computer's move
            4. Show the board again
            5. Go back to step 2.
                -> After each move (human or computer) check for the win
                -> The player who moved last won
                -> If the board is full AND the game was not won, it's a draw.
            6. When the game ends, display the final state of the board and print a corresponding
            message
        """
        print("Welcome to Tic Tac Toe")
        # print the empty board
        print(self._game.get_board())


if __name__ == "__main__":
    # console is the name of a variable of type UI
    console = UI()
    console.start()

    # x = [1, 2, 3]
    # x= list()
