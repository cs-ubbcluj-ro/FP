"""Tests for the numeric type, separate from tests for calculator state."""
from unittest import TestCase, main

from examples.ex38_rational_calc.domain import Rational


class TestRational(TestCase):
    def test_create(self):
        r = Rational(1, 3)
        self.assertEqual(r.num, 1)
        self.assertEqual(r.denom, 3)
        self.assertEqual(str(Rational(4)), "4/1")

    def test_normalization(self):
        cases = [(2, 4, 1, 2), (1, -2, -1, 2),
                 (-2, -4, 1, 2), (0, -3, 0, 1)]
        for numerator, denominator, expected_num, expected_denom in cases:
            r = Rational(numerator, denominator)
            self.assertEqual(r.num, expected_num)
            self.assertEqual(r.denom, expected_denom)

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Rational(1, 0)

    def test_integer_inputs_required(self):
        for numerator, denominator in [(1.5, 2), (1, 2.5), ("1", 2), (1, None)]:
            with self.assertRaises(TypeError):
                Rational(numerator, denominator)

    def test_add_leaves_operands_unchanged(self):
        left = Rational(1, 2)
        right = Rational(1, 3)
        result = left.add(right)
        self.assertEqual(result.num, 5)
        self.assertEqual(result.denom, 6)
        self.assertEqual(str(left), "1/2")
        self.assertEqual(str(right), "1/3")
        self.assertIsNot(result, left)
        self.assertIsNot(result, right)

    def test_add_operator(self):
        self.assertEqual(Rational(1, 3) + Rational(1, 3), Rational(2, 3))
        self.assertEqual(Rational(1, 2) + Rational(-1, 2), Rational(0))

    def test_equality_and_identity(self):
        a = Rational(1, 2)
        b = Rational(2, 4)
        alias = a
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        self.assertIs(a, alias)
        self.assertEqual(Rational(1, -2), Rational(-1, 2))
        self.assertEqual(Rational(-2, -4), a)
        self.assertEqual(Rational(0, -3), Rational(0))
        self.assertNotEqual(a, Rational(1, 3))

    def test_exact_ordering(self):
        self.assertLess(Rational(1, 3), Rational(2, 3))
        self.assertGreater(Rational(2, 3), Rational(1, 3))
        self.assertLess(Rational(1, -2), Rational(0))
        self.assertLess(Rational(2**53), Rational(2**53 + 1))
        self.assertLess(Rational(1, 10**400), Rational(2, 10**400))

    def test_unsupported_operands(self):
        r = Rational(1, 2)
        self.assertNotEqual(r, None)
        self.assertNotEqual(r, 0.5)
        with self.assertRaises(TypeError):
            r + 1
        with self.assertRaises(TypeError):
            1 + r
        with self.assertRaises(TypeError):
            r < None
        with self.assertRaises(TypeError):
            r.add(1)

    def test_read_only_properties(self):
        r = Rational(1, 2)
        with self.assertRaises(AttributeError):
            r.num = 9
        with self.assertRaises(AttributeError):
            r.denom = 0
        self.assertEqual(str(r), "1/2")

    def test_text_and_approximation(self):
        self.assertEqual(str(Rational(2, -4)), "-1/2")
        self.assertEqual(str(Rational(0, -3)), "0/1")
        self.assertEqual(Rational(1, 2).get_float(), 0.5)

    def test_counter_counts_constructions(self):
        before = Rational.get_total_number_of_instances()
        r = Rational(1, 2)
        alias = r
        self.assertIs(alias, r)
        self.assertEqual(Rational.get_total_number_of_instances(), before + 1)
        result = r + r
        self.assertEqual(str(result), "1/1")
        self.assertEqual(Rational.get_total_number_of_instances(), before + 2)

    def test_invalid_constructions_do_not_increment_counter(self):
        before = Rational.get_total_number_of_instances()
        with self.assertRaises(ValueError):
            Rational(1, 0)
        with self.assertRaises(TypeError):
            Rational(1.5)
        self.assertEqual(Rational.get_total_number_of_instances(), before)


if __name__ == "__main__":
    main()
