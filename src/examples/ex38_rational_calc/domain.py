"""Rational values with read-only properties for use by the calculator.

Author: Arthur
"""
from math import gcd


class Rational:
    """Represent an exact rational value using two integers.

    Representation invariant: a positive denominator and a reduced fraction.
    The public interface reads values and creates new ones; it has no setters.
    """

    # Counts successful constructions, not live objects or distinct values.
    _number_of_instances = 0

    def __init__(self, numerator, denominator=1):
        """Initialize numerator/denominator.

        Raise TypeError for non-integers and ValueError for a zero denominator.
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")
        if denominator == 0:
            raise ValueError("Denominator cannot be 0!")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        divisor = gcd(numerator, denominator)
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor
        Rational._number_of_instances += 1

    # Properties provide attribute syntax (r.num) while keeping the storage
    # non-public. No setters: clients create a new Rational to change a value.
    # Underscores remain a convention, not an enforced access restriction.
    @property
    def num(self):
        """Return the numerator of the reduced fraction."""
        return self._numerator

    @property
    def denom(self):
        """Return the positive denominator of the reduced fraction."""
        return self._denominator

    @staticmethod
    def get_total_number_of_instances():
        """Return the number of Rational instances successfully created so far."""
        return Rational._number_of_instances

    def add(self, a):
        """Return the sum as a new Rational; leave both operands unchanged.

        Raise TypeError if a is not a Rational from this example.
        """
        if not isinstance(a, Rational):
            raise TypeError("Can only add another Rational.")
        numerator = (self.num * a.denom
                     + a.num * self.denom)
        denominator = self.denom * a.denom
        return Rational(numerator, denominator)

    def __add__(self, other):
        """Support r1 + r2 using the ordinary add method."""
        if not isinstance(other, Rational):
            # A return value, not an exception: let Python try the other operand.
            return NotImplemented
        return self.add(other)

    def get_float(self):
        """Return a floating-point approximation; it may lose precision."""
        return self.num / self.denom

    def __lt__(self, other):
        """Compare exact values using r1 < r2."""
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.num * other.denom
                < other.num * self.denom)

    def __eq__(self, other):
        """Compare values with ==, rather than identities with is."""
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.num == other.num
                and self.denom == other.denom)

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

