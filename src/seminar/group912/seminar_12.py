"""
Battleship!

What classes you need to write:

    class UI
        - phase 1 -- ship placement
            - manages the user's ship placement (2 ships of length 3 each)
            - ships can be placed both horizontally and vertically
            - ships must be fully contained in the board and not overlap

        - phase 2 -- playing the game
            - human and computer take turns firing at each other
            - human input: "fire C2"
                -> squares that are hit are shown with 'X'
                -> square that were empty are shown with '.'
            - computer may fire at random, but valid squares
                (keep a list of where the computer already fired)
            - game ends when one player's ships are both sunk

    class Game (it's like Services in other programs)
        - phase 1
            - place the computer's ships randomly
        - phase 2
            - fire on the player's ships

    class Board (this is the domain)
        - let's try to use inheritance in order to reuse code

        class Board -> is a 6x6 board that holds 2 ships of 3 squares each
            - boards should have a header row (A B C D E F) and a header column
            (1 2 3 4 5 6), so that we can identify squares easily.

        class PlayerBoard(Board):
            - this is where the human placed their ships
            - this displays the ships as well as where the opponent has hit or missed
            - achieve this by overriding the __str__

        class TargetingBoard(Board):
            - this is where the computer placed its ships
            - this only displays where the human has hit or missed
            - achieve this by overriding the __str__
"""
from texttable import Texttable

board_data = [[0 for i in range(6)] for j in range(6)]

board_data[2][1] = 1
board_data[2][2] = 1
board_data[2][3] = 1

board_data[3][3] = 1
board_data[4][3] = 1
board_data[5][3] = 1

t = Texttable()
for row in board_data:
    t.add_row(row)
print(t.draw())
