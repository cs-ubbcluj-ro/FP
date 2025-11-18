"""
Rational numbers represented as lists
"""
from math import gcd


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
    return {"num": numerator // _gcd, "denom": denominator // _gcd}


def get_numerator(q) -> int:
    return q["num"]


def get_denominator(q) -> int:
    return q["denom"]


def add_rational(q1, q2):
    """
    Return the sum of rational numbers q1 and q2
    >>> add_rational(create_rational(1),create_rational(3))

    :rtype: list[int]
    :param q1: First number
    :param q2: Second number
    :return:
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
    :param q: The number we want represented as a string
    :return:
    """
    return str(get_numerator(q)) + "/" + str(get_denominator(q))
