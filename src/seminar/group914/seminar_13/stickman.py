import texttable


class Stickman:
    def __init__(self):
        self.__table_first_row = ['_', '_', '_', '_']
        self.__table_second_row = ['|', ' ', ' ', ' ']
        self.__table_third_row = ['|', ' ', ' ', ' ']
        self.__table_fourth_row = ['|', ' ', ' ', ' ']
        self.__stage = 0
        self.__stages = [self.__add_head, self.__add_torso, self.__add_left_arm, self.__add_right_arm,
                         self.__add_left_leg,
                         self.__add_right_leg]

    @staticmethod
    def generate_canvas():
        table = texttable.Texttable()
        table.set_chars(['', '', '', ''])
        table.set_cols_align(['l', 'r', 'c', 'l'])
        table.set_cols_valign(['b', 'b', 'm', 't'])
        return table

    def __str__(self):
        table = self.generate_canvas()
        table.add_row(self.__table_first_row)
        table.add_row(self.__table_second_row)
        table.add_row(self.__table_third_row)
        table.add_row(self.__table_fourth_row)
        return table.draw()

    def __add_head(self):
        self.__table_second_row[2] = '()'

    def __add_torso(self):
        self.__table_third_row[2] = '||'

    def __add_left_arm(self):
        self.__table_third_row[1] = '/'

    def __add_right_arm(self):
        self.__table_third_row[3] = '\\'

    def __add_left_leg(self):
        self.__table_fourth_row[2] = 'L'

    def __add_right_leg(self):
        self.__table_fourth_row[2] = 'LL'

    def draw(self):
        try:
            self.__stages[self.__stage]()
            self.__stage += 1
        except IndexError:
            pass  # raise appropriate game error


stick_man = Stickman()
for i in range(6):
    stick_man.draw()
    print(stick_man)
