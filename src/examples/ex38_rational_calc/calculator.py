"""Calculator state and operations, independent of console input/output."""
from examples.ex38_rational_calc.domain import Rational


class Calculator:
    def __init__(self):
        # Each calculator has its own total and history
        self._total = Rational(0)
        self._history = []

    @property
    def total(self):
        """Return the current total without exposing an assignment operation.

        A read-only property alone does not protect the object it returns.
        Here Rational also has no public setters, so clients cannot change
        the total's value through its public interface.
        """
        return self._total

    def add(self, r):
        """Add a Rational and save the previous total for undo.

        Adding zero changes nothing and creates no undo point.
        Raise TypeError if r is not a Rational.
        """
        if not isinstance(r, Rational):
            raise TypeError("Can only add a Rational to the calculator.")
        if r.num == 0:
            return
        # + calls Rational.__add__ and creates a new value.
        # Calculate first so a failed addition does not change the history.
        new_total = self._total + r
        self._history.append(self._total)
        self._total = new_total

    def undo(self):
        """Restore the previous total; raise ValueError if history is empty."""
        if not self._history:
            raise ValueError("No more undo steps!")
        self._total = self._history.pop()

    @staticmethod
    def get_number_count():
        """Return all Rational constructions, across all calculators and clients."""
        return Rational.get_total_number_of_instances()

    def reset(self):
        """Reset the total to zero and discard all undo history.

        Reset itself cannot be undone.
        """
        self._total = Rational(0)
        self._history.clear()
