"""Extend the basic Rational example with operators and class-level information.

Author: Arthur
"""
from math import gcd


class Rational:
    """Represent an exact rational value using two integers.

    Representation invariant: a positive denominator and a reduced fraction.
    The public interface reads values and creates new ones; it has no setters.
    """

    # Counts successful constructions, not live objects or distinct values.
    number_of_instances = 0

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
        Rational.number_of_instances += 1

    def get_numerator(self):
        """Return the numerator of the reduced fraction."""
        return self.__numerator

    def get_denominator(self):
        """Return the positive denominator of the reduced fraction."""
        return self.__denominator

    @staticmethod
    def get_total_number_of_instances():
        """Return the number of Rational instances successfully created so far."""
        return Rational.number_of_instances

    def add(self, a):
        """Return the sum as a new Rational; leave both operands unchanged.

        Raise TypeError if a is not a Rational from this example.
        """
        if not isinstance(a, Rational):
            raise TypeError("Can only add another Rational.")
        numerator = (self.get_numerator() * a.get_denominator()
                     + a.get_numerator() * self.get_denominator())
        denominator = self.get_denominator() * a.get_denominator()
        return Rational(numerator, denominator)

    def __add__(self, other):
        """Support r1 + r2 using the ordinary add method."""
        if not isinstance(other, Rational):
            # A return value, not an exception: let Python try the other operand.
            return NotImplemented
        return self.add(other)

    def get_float(self):
        """Return a floating-point approximation; it may lose precision."""
        return self.get_numerator() / self.get_denominator()

    def __lt__(self, other):
        """Compare exact values using r1 < r2."""
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.get_numerator() * other.get_denominator()
                < other.get_numerator() * self.get_denominator())

    def __eq__(self, other):
        """Compare values with ==, rather than identities with is."""
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.get_numerator() == other.get_numerator()
                and self.get_denominator() == other.get_denominator())

    def __str__(self):
        return str(self.get_numerator()) + "/" + str(self.get_denominator())


def test_create():
    for a, b, numerator, denominator in [(1, 3, 1, 3), (4, 3, 4, 3),
                                         (2, 4, 1, 2), (1, -2, -1, 2),
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
    assert r1 == Rational(1, 2) and r2 == Rational(1, 3)
    assert result is not r1 and result is not r2


def test_equal():
    a = Rational(1, 2)
    b = Rational(2, 4)
    c = a
    assert a == b
    assert a is not b
    assert a is c
    assert Rational(1, -2) == Rational(-1, 2)
    assert Rational(-2, -4) == Rational(1, 2)
    assert Rational(0, -3) == Rational(0)
    assert a != Rational(1, 3)
    # Intentionally use == to test the equality operator with another type.
    assert (a == None) is False
    assert (a == 0.5) is False  # Mixed-type arithmetic/equality is not supported.


def test_compare_operator():
    assert Rational(1, 3) < Rational(2, 3)
    # Python can use the right operand's __lt__ for this > comparison.
    assert Rational(2, 3) > Rational(1, 3)
    assert Rational(1, -2) < Rational(0)
    assert Rational(2**53) < Rational(2**53 + 1)
    assert Rational(1, 10**400) < Rational(2, 10**400)


def test_add_operator():
    assert Rational(1, 3) + Rational(1, 3) == Rational(2, 3)
    assert Rational(1, 2) + Rational(-1, 2) == Rational(0)


def test_text_and_float():
    assert str(Rational(2, -4)) == "-1/2"
    assert str(Rational(0, -3)) == "0/1"
    assert Rational(1, 2).get_float() == 0.5


def test_invalid_values():
    before = Rational.get_total_number_of_instances()
    try:
        Rational(1, 0)
    except ValueError:
        pass
    else:
        assert False, "A zero denominator must raise ValueError."
    try:
        Rational("1", 2)
    except TypeError:
        pass
    else:
        assert False, "A non-integer numerator must raise TypeError."
    assert Rational.get_total_number_of_instances() == before


def test_unsupported_operands():
    r = Rational(1, 2)
    try:
        r + 1
    except TypeError:
        pass
    else:
        assert False, "Adding an int is not supported."
    try:
        r < None
    except TypeError:
        pass
    else:
        assert False, "Ordering with None is not supported."
    try:
        r.add(1)
    except TypeError:
        pass
    else:
        assert False, "The ordinary add method also requires a Rational."


def test_instance_count():
    before = Rational.get_total_number_of_instances()
    r = Rational(1, 2)
    alias = r  # Another name for the same object does not construct a new one.
    assert alias is r
    assert Rational.get_total_number_of_instances() == before + 1
    result = r + r
    assert str(result) == "1/1"
    assert Rational.get_total_number_of_instances() == before + 2


if __name__ == "__main__":
    test_create()
    test_rational_add()
    test_equal()
    test_compare_operator()
    test_add_operator()
    test_text_and_float()
    test_invalid_values()
    test_unsupported_operands()
    test_instance_count()
    print("All operator Rational tests passed.")
    print("Total instances created:", Rational.get_total_number_of_instances())
