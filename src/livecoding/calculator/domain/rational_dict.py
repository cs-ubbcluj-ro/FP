def create_rational(numerator: int = 0, denominator: int = 1):
    """
    Create and return a new domain number
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
    # FIXME Simplify the domain number
    return {"num": numerator, "denom": denominator}


def get_numerator(q):
    """
    Return the numerator
    Args:
        q: The domain number

    Returns:
        The numerator (int)
    """
    return q["num"]


def get_denominator(q):
    return q["denom"]
