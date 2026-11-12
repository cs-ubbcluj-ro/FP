"""

Create a calculator program for rational numbers with the following
functionalities:
    + add a rational number to the calculator
    u undo the last operation
    x exit


Design rules:
    - Pass dependencies as parameters; do not use mutable global state.
    - Rational operations return new values and never modify existing rationals.
    - Calculator operations deliberately modify the supplied calculator.
    - Non-UI functions neither perform I/O nor call UI functions.
    - Access rational components only through the representation functions.
"""


# ------------------------------------------------------------
# Rational numbers: representation and non-UI program logic
# ------------------------------------------------------------

def create_rational(numerator: int = 0, denominator: int = 1):
    """
    Create and return a new rational number
    Args:
        numerator: The int numerator (default value 0)
        denominator: The int denominator (default value 1). Denominator must be non-zero!

    Returns:
        The created number

    Raises:
        ValueError in case the denominator was 0
    """
    if denominator == 0:
        # ValueError is a Python exception
        # Exceptions are raised when something went wrong
        # What happens when the exception was raised?
        #   (1) The function exits immediately without returning anything
        #   (2) The calling function must handle (try ... except) the ValueError, otherwise
        #   it too returns immediately
        #   (3) If no program function handled the exception, the program crashes
        raise ValueError("Denominator cannot be 0")
    # FIXME Simplify the rational number
    return {"num": numerator, "denom": denominator}
    # return [numerator, denominator]


def get_numerator(q):
    """
    Return the numerator
    Args:
        q: The rational number

    Returns:
        The numerator (int)
    """
    # return q[0]
    return q["num"]


def get_denominator(q):
    # return q[1]
    return q["denom"]


def to_str(q) -> str:
    # FIXME Improve the representation (return 2, not 2/1, put the - sign in front of the numerator)
    # return str(get_numerator(q)) + "/" +str(get_denominator(q))
    return f"{get_numerator(q)}/{get_denominator(q)}"


def add_rational(q1, q2):
    # Python functions are first class citizens (they can be used like any variable, assigned, used as
    # parameters etc.)

    gn = get_numerator  # function assignment, not call!
    gd = get_denominator
    # In Python, () is the call operator

    new_numerator = gn(q1) * gd(q2) + gn(q2) * gd(q1)
    new_denominator = gd(q1) * gd(q2)
    return create_rational(new_numerator, new_denominator)


"""
    Test function for the rational data type
    
    What to know about test functions:
        1. Names should start with test_
        2. Must not take any parameters or return anything (they must work automatically)
        3. They should be runnable in any order (don't depend on each other)
        4. They should raise AssertionError in case the program does not behave as expected
        
    NB! This kind of testing is called "unit testing"
    NB! We will work to improve these :)
"""


def test_rational():
    q = create_rational(2, 3)
    """
    What does the assert keyword do?
        assert <condition>
        
    If <condition> is True  => program continues, nothing visible happens => TEST PASSED
    If <condition> is False => AssertionError is raised, program crashes => TEST FAILED 
    """
    assert get_numerator(q) == 2
    assert get_denominator(q) == 3

    q = create_rational(9)
    assert get_numerator(q) == 9
    assert get_denominator(q) == 1

    q = create_rational()
    assert get_numerator(q) == 0
    assert get_denominator(q) == 1


def test_rational_add():
    q1 = create_rational(1, 2)
    q2 = create_rational(1, 2)
    q_sum = add_rational(q1, q2)

    assert get_numerator(q_sum) == 4
    assert get_denominator(q_sum) == 4


test_rational()
test_rational_add()

q1 = create_rational(1, 2)
q2 = create_rational(1, 2)
q_sum = add_rational(q1, q2)
print(to_str(q_sum))


# ------------------------------------------------------------
# Calculator: explicit state and intentional mutation
#
# The calculator stores:
#   (1) current value : rational number (initially 0, when starting the program)
#   (2) history of previous values: list<rational numbers>
# ------------------------------------------------------------
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
    calculator["value"] = q
    calculator["history"].append(q)  # add the value to the undo list


def add_calculator(calculator, q):
    """
    Add a number to the calculator. The calculator is updated with the new sum and number history
    Args:
        calculator: The calculator's state
        q: The rational number
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


test_calculator()


# ------------------------------------------------------------
# UI: read/display data and delegate computations to non-UI functions
# ------------------------------------------------------------


def print_menu():
    print("Calculator menu:")
    print("   + add a rational number")
    print("   u undo last operation")
    print("   x close the calculator")
