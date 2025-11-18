# import rational_as_list
# import rational_as_dict

# import * imports all names that don't start with _
from rational_as_dict import create_rational, to_str, add_rational
# from rational_as_list import create_rational, add_rational


def create_calculator():
    return {"value": create_rational(0), "history": []}


def get_calculator_value(calculator):
    return calculator["value"]


def set_calculator_value(calculator, new_value):
    calculator["value"] = new_value


def get_calculator_history(calculator):
    return calculator["history"]


def add_to_calculator(calculator, q):
    """
    Add a value to the calculator
    @param: calculator - The current calculator
    @param: q - The rational number we add
    """
    val = get_calculator_value(calculator)
    set_calculator_value(calculator, add_rational(val, q))
    # add the old value in the calculator to the history list
    get_calculator_history(calculator).append(val)


def test_calculator():
    calc = create_calculator()
    assert get_calculator_value(calc) == create_rational(0)

    add_to_calculator(calc, create_rational(1, 3))
    assert get_calculator_value(calc) == create_rational(1, 3)

    add_to_calculator(calc, create_rational(0))
    assert get_calculator_value(calc) == create_rational(1, 3)

    add_to_calculator(calc, create_rational(-1, 3))
    assert get_calculator_value(calc) == create_rational(0)


if __name__ == "__main__":
    """
    Separate running the tests from running the program
    """
    test_calculator()
