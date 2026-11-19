"""First Rational implementation: initialization, getters and an ordinary method.

Author: Arthur
"""
from math import gcd


class Rational:
    """Represent an exact rational value using two integers.

    Representation invariant: the denominator is positive and the fraction
    is reduced. In particular, zero is represented as 0/1.
    """

    def __init__(self, a, b=1):
        """Initialize a/b; raise TypeError for non-integers or ValueError if b is 0."""
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Numerator and denominator must be integers.")
        if b == 0:
            raise ValueError("Denominator cannot be 0!")
        if b < 0:
            a, b = -a, -b
        divisor = gcd(a, b)
        self.__numerator = a // divisor
        self.__denominator = b // divisor

    def get_numerator(self):
        """Return the numerator of the reduced fraction."""
        return self.__numerator

    def get_denominator(self):
        """Return the positive denominator of the reduced fraction."""
        return self.__denominator

    def add(self, a):
        """Return self + a as a new Rational, leaving both operands unchanged.

        a must be a Rational from this example; otherwise raise TypeError.
        """
        if not isinstance(a, Rational):
            raise TypeError("Can only add another Rational.")
        numerator = (self.get_numerator() * a.get_denominator()
                     + a.get_numerator() * self.get_denominator())
        denominator = self.get_denominator() * a.get_denominator()
        return Rational(numerator, denominator)


def test_create():
    r = Rational(1, 3)
    assert r.get_numerator() == 1
    assert r.get_denominator() == 3
    r = Rational(4, 3)
    assert r.get_numerator() == 4
    assert r.get_denominator() == 3


def test_normalization():
    for a, b, numerator, denominator in [(2, 4, 1, 2), (1, -2, -1, 2),
                                         (-2, -4, 1, 2), (0, -3, 0, 1)]:
        r = Rational(a, b)
        assert r.get_numerator() == numerator
        assert r.get_denominator() == denominator


def test_rational_add():
    r1 = Rational(1, 2)
    r2 = Rational(1, 3)
    result = r1.add(r2)
    assert result.get_numerator() == 5
    assert result.get_denominator() == 6
    assert r1.get_numerator() == 1 and r1.get_denominator() == 2
    assert r2.get_numerator() == 1 and r2.get_denominator() == 3
    assert result is not r1 and result is not r2


def test_invalid_values():
    try:
        Rational(1, 0)
    except ValueError:
        pass  # Expected: a zero denominator is invalid.
    else:
        assert False, "A zero denominator must raise ValueError."
    try:
        Rational(1.5, 2)
    except TypeError:
        pass
    else:
        assert False, "A non-integer numerator must raise TypeError."
    try:
        Rational(1, 2).add(1)
    except TypeError:
        pass
    else:
        assert False, "add expects another Rational."


if __name__ == "__main__":
    test_create()
    test_normalization()
    test_rational_add()
    test_invalid_values()
    print("All basic Rational tests passed.")
