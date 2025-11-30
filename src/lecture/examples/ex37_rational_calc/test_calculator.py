from unittest import TestCase

from lecture.examples.ex37_rational_calc.domain import Rational


class TestCalculator(TestCase):
    def test_rational_add(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        r3 = r1.add(r2)
        assert r3.num == 5
        assert r3.denom == 6
        assert r3 == Rational(5, 6)

    def test_equal(self):
        """
          test function for testing == for 2 rational numbers
        """
        r1 = Rational(1, 3)
        assert r1 == r1
        r2 = Rational(1, 3)
        assert r1 == r2
        r1 = Rational(1, 3)
        r1 = r1.add(Rational(2, 3))
        r2 = Rational(1, 1)
        assert r1 == r2

    def test_compare_operator(self):
        """
        Test function for < >
        """
        r1 = Rational(1, 3)
        r2 = Rational(2, 3)
        assert r2 > r1
        assert r1 < r2

    def test_add_operator(self):
        """
          Test function for the + operator
        """
        r1 = Rational(1, 3)
        r2 = Rational(1, 3)
        r3 = r1 + r2
        assert r3 == Rational(2, 3)

    def test_create(self):
        """
          Test function for creating rational numbers
        """
        r1 = Rational(1, 3)  # create the rational number 1/3
        assert r1.num == 1
        assert r1.denom == 3
        r1 = Rational(4, 3)  # create the rational number 4/3
        assert r1.num == 4
        assert r1.denom == 3
