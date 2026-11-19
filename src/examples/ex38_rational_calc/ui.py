"""Console interaction: use the calculator's public interface."""
from examples.ex38_rational_calc.calculator import Calculator
from examples.ex38_rational_calc.domain import Rational


class UI:
    def __init__(self, calculator):
        self._calculator = calculator
        self._commands = {"+": self.add_number, "c": self.clear,
                          "u": self.undo, "?": self.count}

    def _print_menu(self):
        print("Calculator:")
        print("   + to add a rational number")
        print("   c to clear the total and undo history")
        print("   u to undo the last addition")
        print("   ? to count all rational numbers created")
        print("   x to close the calculator")

    def add_number(self):
        numerator = int(input("Give numerator: "))
        denominator = int(input("Give denominator: "))
        self._calculator.add(Rational(numerator, denominator))

    def undo(self):
        self._calculator.undo()

    def clear(self):
        self._calculator.reset()

    def count(self):
        print("Number of Rational instances created so far:",
              self._calculator.get_number_count())

    def start(self):
        # Use the supplied calculator's existing state; do not reset it here.
        while True:
            self._print_menu()
            print("Total:", self._calculator.total)  # Uses Rational.__str__.
            command = input("Command: ").strip().lower()
            if command == "x":
                return
            if command not in self._commands:
                print("Bad command")
                continue
            try:
                self._commands[command]()
            except ValueError as error:
                # Invalid integers, a zero denominator, or an empty undo history.
                print("Error:", error)


if __name__ == "__main__":
    calc = Calculator()
    ui = UI(calc)
    ui.start()
