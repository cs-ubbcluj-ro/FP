"""
Handle the program's user interaction
    - display the board (use texttable module)
    - ask user for their move
    - when the game is finished => send the user a message, and exit
"""
from texttable import Texttable

"""
How the program UI is supposed to work
    1. Import functions from the game module and board module
    2. Initialize an empty game board
    3. Start the game (in a loop):
        a. Display the (at first empty) board
        b. Ask for the human player's move (human plays with 'X')
            - if error => ask for move again
        c. Make the computer's move, using the function in game
        module (computer plays with 'O')
        d. After each move (steps b., c.) check if the board is won or
        the board is full => display corresponding message and stop
        the program
"""

from texttable import Texttable

table = Texttable()
table.add_row([' ', ' ', ' '])
table.add_row([' ', 'X', ' '])
table.add_row([' ', ' ', 'O'])
print(table.draw())
