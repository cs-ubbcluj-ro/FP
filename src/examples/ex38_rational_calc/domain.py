"""
Created on Oct 30, 2019

@author: Arthur
"""
from math import gcd


class Rational:
    """
      Abstract data type rational numbers
      Domain: {a/b  where a,b integer numbers, b!=0, greatest common divisor a, b =1}
    """

    # Class field is shared by all instances
    _number_of_instances = 0

    def __init__(self, numerator, denominator=1):
        """
          Initialise a rational number
          numerator, denominator integers, denominator non-zero
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be 0!")

        d = gcd(numerator, denominator)
        self.num = numerator // d
        self.denom = denominator // d
        Rational._number_of_instances += 1

    @property
    def num(self):
        return self._numerator

    @num.setter
    def num(self, value):
        self._numerator = value

    @property
    def denom(self):
        return self._denominator

    @denom.setter
    def denom(self, value):
        if value == 0:
            raise ValueError("Denominator cannot be 0!")
        self._denominator = value

    @staticmethod
    def get_total_number_of_instances():
        """
          Get the number of created rational number instances
          return integer
        """
        return Rational._number_of_instances

    def add(self, a):
        """
        add 2 rational numbers
        a is a rational number
        Return the sum of two rational numbers as an instance of rational number.
        Raise ValueError if the denominators are zero.
        """
        return Rational(self.num * a.denom + self.denom * a.num, self.denom * a.denom)

    def __add__(self, other):
        """
          Overload + operator
          other  - rational number
          return a rational number, the sum of self and other
        """
        return self.add(other)

    def get_float(self):
        """
          Get the real value for the rational number
          return a float
        """
        return float(self.num) / self.denom

    def __lt__(self, ot):
        """
          Compare 2 rational numbers (less than)
          self the current instance
          ot a rational number
          return True if self<ot, False otherwise
        """
        return self.get_float() < ot.get_float()

    def __str__(self):
        """
          provide a string representation for the rational number
          return a string
        """
        return str(self.num) + "/" + str(self.denom)

    def __eq__(self, other):
        """
          Verify if 2 rational numbers are equals
          other - a rational number
          return True if the instance is equal with other
        """
        return self.num == other.num and self.denom == other.denom
