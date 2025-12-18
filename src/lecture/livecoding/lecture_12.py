import string
from random import shuffle

from texttable import Texttable


class MinefieldException(Exception):
    pass


class Minefield:
    def __init__(self, rows: int, columns: int, mines: int):
        self.__rows = rows
        self.__columns = columns
        self.__mines = mines

        # We did not lay the mines
        self.__mines_laid = False

        self.__data = [[0 for i in range(columns)] for j in range(rows)]

    def __cell_state(self, row, column):
        val = self.__data[row][column]
        if val < 10:
            return val, False  # returns a tuple
        else:
            return val - 10, True

    def click(self, row: int, column: int):
        if not (0 < row < self.__rows) or not (0 < column < self.__columns):
            raise MinefieldException(f"User clicked out of bounds: ({row},{column})")
        self.__lay_mines(row, column)

        if self.__cell_state(row, column)[0] == 9:
            raise MinefieldException(f"Game over, there is a mine on ({row},{column})")
        # reveal part of the minefield
        self.__reveal(row, column)

    def __reveal(self, row: int, column: int):
        value, rev = self.__cell_state(row, column)

        if not rev:
            self.__data[row][column] += 10
        else:
            # stop the recursion if the cell was already revealed
            return
        if value > 0:
            # if there is at least one adjacent mine, we only reveal the current cell
            return

        # flood fill all the way to the closest mines or the minefield border
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    # we are on the same, mined square
                    continue
                if not (0 <= row + dy < self.__rows) or not (0 <= column + dx < self.__columns):
                    # we are outside the playing field
                    continue
                self.__reveal(row + dy, column + dx)

    def __lay_mines(self, row: int, column: int):
        if self.__mines_laid:
            # if we already laid the mines => quit
            return

        self.__mines_laid = True
        # build list of all valid coordinates for mines
        locations = []
        for i in range(self.__rows):
            for j in range(self.__columns):
                if abs(row - i) <= 1 and abs(column - j) <= 1:
                    # continue -- move to the next iteration of the innermost loop
                    continue
                locations.append((i, j))
        shuffle(locations)

        # actually lay the mines
        for i in range(self.__mines):
            mine_row, mine_column = locations.pop()  # tuple unpacking
            self.__data[mine_row][mine_column] = 9  # 9 means the square is mined

            # calculate the number of mines adjacent to this square
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        # we are on the same, mined square
                        continue
                    if not (0 <= mine_row + dy < self.__rows) or not (0 <= mine_column + dx < self.__columns):
                        # we are outside the playing field
                        continue
                    if self.__data[mine_row + dy][mine_column + dx] == 9:
                        # we are on a mine
                        continue
                    self.__data[mine_row + dy][mine_column + dx] += 1

    def __get_header_row(self):
        # TODO Fix crash if more than 27 columns
        return '/' + string.ascii_uppercase[0:self.__columns]

    def __str__(self):
        t = Texttable()
        t.header(self.__get_header_row())
        # for row in self.__data:
        #     t.add_row(row)
        # return t.draw()

        index = 1
        for row in self.__data:
            """
            0 - 9   -> #
            10      -> ' ' (space character)
            11 - 18 -> 1 - 8
            """
            visible_row = [str(index)]
            index += 1
            for val in row:
                if val < 10:
                    visible_row += '#'
                elif val == 10:
                    visible_row += ' '
                else:
                    visible_row += str(val - 10)
            t.add_row(visible_row)
        return t.draw()


if __name__ == "__main__":
    m = Minefield(8, 10, 10)
    m.click(2, 2)
    print(m)
