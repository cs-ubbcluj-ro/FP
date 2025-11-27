from lecture.livecoding.lecture8.rational import Rational


class CalculatorError(Exception):
    """
    CalculatorError is a kind of Exception
    Exception is the Python builtin class for Errors
    """
    pass


class Calculator:
    def __init__(self):
        self._value = Rational(0)
        # History of the calculator's operations
        self._history = []

    def add_number(self, value):
        # record the value in the undo list
        self._history.append(self.value)
        # update calculator value
        self._value += value

    @property
    def value(self):
        return self._value

    def undo(self):
        if len(self._history) == 0:
            # there are no operations to undo
            # raise CalculatorError("No operations to undo")
            raise ValueError("No operations to undo")
        self._value = self._history.pop()


c = Calculator()
print(c.value)


def test_calculator():
    c = Calculator()
    try:
        c.undo()
        # in case we don't raise an exception
        assert False
    except CalculatorError:
        # this is what we expected
        assert True
    except Exception:
        # we expect a CalculatorError, and not any type of error
        assert False

test_calculator()