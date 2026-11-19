# ------------------------------------------------------------
# Calculator: explicit state and intentional mutation
#
# The calculator stores:
#   (1) current value : domain number (initially 0, when starting the program)
#   (2) history of previous values: list<domain numbers>
# ------------------------------------------------------------
from livecoding.calculator.domain.rational_dict import create_rational, get_denominator, get_numerator
from livecoding.calculator.domain.rational import add_rational


def create_calculator():
    """
    Initialize a new calculator with value 0/1 and no undo history
    Returns:
        The new calculator
    """
    return {"value": create_rational(), "history": []}


def get_value_calculator(calculator):
    return calculator["value"]


def set_value_calculator(calculator, q):
    calculator["history"].append(get_value_calculator(calculator))  # add the value to the undo list
    calculator["value"] = q


def undo_calculator(calculator):
    if len(calculator["history"]) == 0:
        raise ValueError("No undos available")

    last_value = calculator["history"].pop()  # removes and returns the last element
    calculator["value"] = last_value


def add_calculator(calculator, q):
    """
    Add a number to the calculator. The calculator is updated with the new sum and number history
    Args:
        calculator: The calculator's state
        q: The domain number
    """
    new_value = add_rational(get_value_calculator(calculator), q)
    set_value_calculator(calculator, new_value)


def test_calculator():
    c = create_calculator()
    add_calculator(c, create_rational(1, 2))
    add_calculator(c, create_rational(1, 2))

    val = get_value_calculator(c)
    assert get_numerator(val) == 4
    assert get_denominator(val) == 4


if __name__ == "__main__":
    test_calculator()
    print("Calculator tests pass!")
