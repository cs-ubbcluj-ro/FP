"""
    Game -- Chomp!
    http://www.papg.com/chomp.html

    What classes you should have (layered architecture)

    class UI
        - handles the turn by turn play
        - uses the Board's __str__ method to draw the board on screen
        - displays win/lose message

    class Game
        - code to make computer think its next move
        - computer can play random but valid moves (like minimal requirement in A11)
            -> make it win if possible

    class Board
        - use Texttable to represent the board
        - have a header (first row & first column) (A B C D ... and 1 2 3 4 ...)
        - raise a GameOverException when the game is over
        - have an __str__ method to display the board using the Texttable
        - human plays with X, computer plays with O
        - the Board size should be customizable
"""
