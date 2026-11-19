"""Test calculator behavior through its public interface."""
from unittest import TestCase, main

from examples.ex38_rational_calc.calculator import Calculator
from examples.ex38_rational_calc.domain import Rational


class TestCalculator(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_initial_total_is_zero(self):
        self.assertEqual(self.calculator.total, Rational(0))

    def test_add_updates_total(self):
        self.calculator.add(Rational(1, 2))
        self.calculator.add(Rational(1, 3))
        self.assertEqual(self.calculator.total, Rational(5, 6))

    def test_undo_restores_previous_total(self):
        self.calculator.add(Rational(1, 2))
        self.calculator.add(Rational(1, 3))
        self.calculator.undo()
        self.assertEqual(self.calculator.total, Rational(1, 2))
        self.calculator.undo()
        self.assertEqual(self.calculator.total, Rational(0))

    def test_undo_without_history_raises(self):
        with self.assertRaises(ValueError):
            self.calculator.undo()
        self.assertEqual(self.calculator.total, Rational(0))

    def test_add_zero_does_not_create_undo_step(self):
        self.calculator.add(Rational(0, -3))
        with self.assertRaises(ValueError):
            self.calculator.undo()
        self.calculator.add(Rational(1, 2))
        self.calculator.add(Rational(0))
        self.calculator.undo()
        self.assertEqual(self.calculator.total, Rational(0))
        with self.assertRaises(ValueError):
            self.calculator.undo()

    def test_zero_addition_does_not_construct_temporary_numbers(self):
        zero = Rational(0)
        before = Rational.get_total_number_of_instances()
        self.calculator.add(zero)
        self.assertEqual(Rational.get_total_number_of_instances(), before)

    def test_reset_clears_history(self):
        self.calculator.add(Rational(1, 2))
        self.calculator.add(Rational(1, 3))
        self.calculator.reset()
        self.assertEqual(self.calculator.total, Rational(0))
        with self.assertRaises(ValueError):
            self.calculator.undo()
        self.calculator.add(Rational(2))
        self.calculator.undo()
        self.assertEqual(self.calculator.total, Rational(0))

    def test_calculators_have_independent_state(self):
        other = Calculator()
        self.calculator.add(Rational(1, 2))
        other.add(Rational(1, 3))
        self.calculator.undo()
        self.assertEqual(self.calculator.total, Rational(0))
        self.assertEqual(other.total, Rational(1, 3))
        other.undo()
        self.assertEqual(other.total, Rational(0))

    def test_invalid_addition_preserves_total_and_history(self):
        self.calculator.add(Rational(1, 2))
        total_before = self.calculator.total
        with self.assertRaises(TypeError):
            self.calculator.add(1)
        self.assertIs(self.calculator.total, total_before)
        self.calculator.undo()
        self.assertEqual(self.calculator.total, Rational(0))
        with self.assertRaises(ValueError):
            self.calculator.undo()

    def test_total_cannot_be_assigned_through_property(self):
        with self.assertRaises(AttributeError):
            self.calculator.total = Rational(10)
        self.assertEqual(self.calculator.total, Rational(0))

    def test_returned_value_cannot_corrupt_undo_through_public_interface(self):
        self.calculator.add(Rational(1, 2))
        earlier_total = self.calculator.total
        self.calculator.add(Rational(1, 3))
        with self.assertRaises(AttributeError):
            earlier_total.num = 9
        with self.assertRaises(AttributeError):
            earlier_total.denom = 3
        self.calculator.undo()
        self.assertIs(self.calculator.total, earlier_total)
        self.assertEqual(self.calculator.total, Rational(1, 2))

    def test_instance_count_is_shared_across_calculators(self):
        before = self.calculator.get_number_count()
        other = Calculator()  # Constructs one initial Rational total.
        self.assertEqual(other.get_number_count(), before + 1)
        self.assertEqual(self.calculator.get_number_count(), before + 1)


if __name__ == "__main__":
    main()
