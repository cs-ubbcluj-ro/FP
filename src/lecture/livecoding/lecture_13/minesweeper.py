from random import shuffle

from texttable import Texttable


class Minefield:
    def __init__(self, rows: int, cols: int, mines: int):
        self.__rows = rows
        self.__cols = cols
        self.__mines = mines

        # have the mines been lain?
        self.__mine_flag = False

        """
        What do we represent inside self.__data?
        0 - 8 -> how many mines are adjacent, for a square that is not mined
        9     -> the square is mined
        
        """
        self.__data = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

        """
        The matrix below is used for actually displaying the minefield to the user
        """
        self.__revealed = [['*' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def __lay_mines(self, clear_row: int, clear_col: int):
        """
        Lay the mines. (clear_row, clear_col) is where the user clicked first. There must be no mine here or adjacent
        :return:
        """
        locations = []
        for i in range(self.__rows):
            for j in range(self.__cols):
                if abs(clear_row - i) <= 1 and abs(clear_col - j) <= 1:
                    # there must be no mines on (clear_row, clear_col) or adjacent to this square
                    # These are the coordinates of the player's first click :)
                    continue
                locations.append((i, j))
        shuffle(locations)
        m = self.__mines
        while m > 0:
            row, col = locations.pop()  # tuple unpacking
            self.__data[row][col] = 9  # lay a mine
            m -= 1

            # add adjacency information for the freshly lain mine
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if not (0 <= row + dx < self.__rows and 0 <= col + dy < self.__cols):
                        continue
                    if self.__data[row + dx][col + dy] == 9:
                        # if the square has a mine, we aren't interested in its adjacency
                        continue
                    # increase the number of adjacent mines
                    self.__data[row + dx][col + dy] += 1

    def click(self, row: int, column: int):
        # TODO Check that (row, column) is unrevealed
        if self.__mine_flag is False:
            # lay the mines the first time the user clicks in the minefield
            self.__lay_mines(row, column)
            self.__mine_flag = True

        # reveal the correct part of the minefield
        # TODO Validate coordinates inside the field :)
        if self.__data[row][column] == 9:
            raise ValueError("Game over, man!")  # TODO Have a GameOverException class :)

        if 0 < self.__data[row][column]:
            # we have at least 1 adjacent mine => we only reveal this square
            self.__revealed[row][column] = self.__data[row][column]
            return

        # if we are here, it means we are on a square with no adjacent mines
        queue = [(row, column)]

        while len(queue) > 0:
            row, col = queue.pop()
            self.__revealed[row][col] = ' '  # mark the square as having no adjacent mines

            # look at all the neighbours of this square
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    if not (0 <= row + dx < self.__rows and 0 <= col + dy < self.__cols):
                        continue
                    if self.__revealed[row + dx][col + dy] != "*":
                        continue
                    if 0 < self.__data[row + dx][col + dy] < 9:
                        self.__revealed[row + dx][col + dy] = self.__data[row + dx][col + dy]
                    if self.__data[row + dx][col + dy] == 0:
                        queue.append((row + dx, col + dy))


    def __str__(self):
        t = Texttable()
        for row in self.__revealed:
            t.add_row(row)
        return t.draw()


mines = Minefield(8, 10, 2)

"""
Lazy loading -- the program should not do work that might be superfluous unless we know its needed
Eager initialization -- do the work preemptively, so that when the user actually needs it, it's already done :)

"""
mines.click(2, 2)
print(mines)
