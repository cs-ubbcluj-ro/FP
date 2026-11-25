from livecoding.calculator_oop.rational import Rational


class Calculator:
    def __init__(self):
        # The value stored by the calculator
        self.__value = Rational()
        # The value history for undo
        self.__history = []

    def get_value(self):
        return self.__value


calc = Calculator()
print(calc)

print(calc.get_value())
