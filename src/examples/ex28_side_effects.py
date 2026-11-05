"""
Rebinding, mutation, and returning a new value.
Adapted from http://www.python-course.eu/passing_arguments.php

Before each call, predict:
  - What value is returned?
  - Does the caller's list change?
  - What will a second name for the same list observe?

These three functions do no I/O. The demonstration prints their results.
Side effects include changes to shared objects and I/O; they are not always
mistakes, but should be deliberate and documented.
"""


def rebind_parameter(values: list) -> None:
    """Rebind the local parameter; leave the input list unchanged; return None."""
    values = [0, 1, 2, 3]
    # This binding disappears when the call finishes. The caller receives no
    # replacement value because the function has no return statement.


def mutate_list(values: list) -> None:
    """Append 999 to the input list in place; return None."""
    values.append(999)


def with_extra_value(values: list) -> list:
    """Return a new list ending in 999; leave the input list unchanged."""
    return values + [999]


def main():
    values = [0, 1, 2]
    alias = values  # Two names, ONE list: this assignment does not copy it.

    result = rebind_parameter(values)
    print("After rebinding:", values, alias, "returned:", result)
    # [0, 1, 2], [0, 1, 2], None

    result = with_extra_value(values)
    print("After creating a list:", values, alias, "returned:", result)
    # [0, 1, 2], [0, 1, 2], [0, 1, 2, 999]
    print("Returned the original object?", result is values)  # False

    result = mutate_list(values)
    print("After mutation:", values, alias, "returned:", result)
    # [0, 1, 2, 999], [0, 1, 2, 999], None
    print("Both names still share one object?", alias is values)  # True


if __name__ == "__main__":
    main()
