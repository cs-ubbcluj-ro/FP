"""

Create a calculator program for rational numbers with the following
functionalities:
    + add a rational number to the calculator
    u undo the last operation
    x exit
"""
from math import gcd


# ----------------------#
# Non-UI functions here #
# ----------------------#

# Functions to handle rational numbers
def create_rational(numerator: int, denominator: int = 1):
    """
    Create a rational number
    @param: numerator - The numerator
    @param: denominator - The denominator, it cannot be 0
    Returns the number represented as a list
    Raises ValueError in case denominator was 0
    """
    if denominator == 0:
        raise ValueError("Cannot create rational number with denominator 0")
    _gcd = gcd(numerator, denominator)
    return [numerator // _gcd, denominator // _gcd]


def get_numerator(q) -> int:
    return q[0]


def get_denominator(q) -> int:
    return q[1]


def add_rational(q1, q2):
    """
    Return the sum of rational numbers q1 and q2
    """
    gn = get_numerator  # Python functions are first-class citizens :)
    gd = get_denominator
    # first-class citizens == can be used just like variables (send as parameters, return, assignment)
    # type of gn after the assignment is function
    # gn is not called unless we use the call operator ->  ()
    return create_rational(gn(q1) * gd(q2) + gn(q2) * gd(q1), gd(q1) * gd(q2))


def to_str(q) -> str:
    """
    Return the str representation of the rational number
    """
    return str(get_numerator(q)) + "/" + str(get_denominator(q))


q = None
try:
    q = create_rational(4, 40)
except ValueError as ve:
    print(ve)

# print(to_str(q))

# Test functions for rational number
"""
    Test functions 101
        1. Test functions should be named test_<something>
        2. Test functions take no parameters and return nothing :(
        3. Use the assert keyword to test things
            assert <boolean_condition>
                if boolean_condition == true => success
                if boolean_condition == false => test fails,
                    AssertionError is raised => program crash :(
        4. A complete program should have test functions for all
        non-trivial program logic
            trivial = setters/getters, simple function 
                    
        5. What we can (and will) still improve on here:
            a. Run test functions autoamtically
            b. Run all test functions, regardless of test failures
            c. Separate test functions from program code
            d. Be able to run tests and the program separately
            e. How do I know I have enough tests ???
"""


def test_rational():
    q = create_rational(1, 2)
    assert get_numerator(q) == 1, get_numerator(q)
    assert get_denominator(q) == 2
    assert to_str(q) == "1/2"

    q = create_rational(20, 5)
    assert get_numerator(q) == 4
    assert get_denominator(q) == 1
    assert to_str(q) == "4/1"

    # Test that trying to create a number with denom = 0 does not work
    try:
        create_rational(1, 0)
        assert False  # this should not be executed
    except ValueError:
        # An exception was raised, exactly as expected
        assert True


def test_add_rational():
    q1 = create_rational(1, 2)
    q2 = create_rational(1, 2)
    assert add_rational(q1, q2) == create_rational(1)

    q1 = create_rational(1, 200)
    q2 = create_rational(1)
    assert add_rational(q1, q2) == create_rational(201, 200)


test_rational()
test_add_rational()


# print(to_str(add_rational(create_rational(99, 100), create_rational(1, 100))))


# Functions to handle the calculator
# calculator stores: (1) current value : rational number, (2) history of previous values: list<rational numbers>

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


test_calculator()


# -----------------------#
# Only UI functions here #
# -----------------------#


def print_menu():
    print("Calculator menu:")
    print("   + add a rational number")
    print("   u undo last operation")
    print("   x close the calculator")


def add_number_ui(calculator):
    # TODO Make sure we add additional checks here
    value = input("Enter number (a/b format):")
    tokens = value.split("/")
    # FIXME denominator is 0 --- halp!
    q = create_rational(int(tokens[0]), int(tokens[1]))
    add_to_calculator(calculator, q)


def undo_ui(calculator):
    pass


def start():
    calculator = create_calculator()
    commands = {"+": add_number_ui, "u": undo_ui}

    while True:
        print_menu()
        print("TOTAL: " + to_str(get_calculator_value(calculator)))
        option = input(">").strip()
        if option in commands:
            try:
                commands[option](calculator)
            except ValueError as a:
                print(a)
        elif option == "x":
            print("Bye!")
            return
        else:
            print("Invalid input")


start()
