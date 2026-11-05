"""
Parameter passing: local names are bound to the supplied objects.
Adapted from http://www.python-course.eu/passing_arguments.php

Predict the caller's value after each call, then run the program.
Integers and lists use the SAME passing mechanism. Assignment to a parameter
rebinds that local name; it does not rebind the caller's variable.
No copy of an argument object is made merely because it is passed to a function.

The prints are tracing aids (and are themselves I/O side effects).
id() identifies an object; do not predict its numeric value or treat it as a
portable memory address. Compare identities of objects that are still alive.
"""


def rebind_integer(number: int):
    """Trace local rebinding; leave the caller's binding unchanged."""
    print("Inside, before assignment:", number, "identity:", id(number))
    number = 42
    print("Inside, after assignment: ", number, "identity:", id(number))


def rebind_list(values: list):
    """Trace local rebinding; leave the caller's list unchanged."""
    print("Inside, before assignment:", values, "identity:", id(values))
    values = [9, 9]
    print("Inside, after assignment: ", values, "identity:", id(values))


def add_element_to_list(values: list):
    # This does not rebind the list, but calls the append() method and modifies its
    # internal state
    # NB! Python entities are classes and objects
    values.append(99)


def main():
    number = 10
    print("Caller, before:", number, "identity:", id(number))
    rebind_integer(number)
    print("Caller, after: ", number, "identity:", id(number))  # Still 10.

    print()
    values = [1, 2]
    print("Caller, before:", values, "identity:", id(values))
    rebind_list(values)
    print("Caller, after: ", values, "identity:", id(values))  # Still [1, 2].

    print()
    values = [1, 2]
    print("Caller, before:", values, "identity:", id(values))
    add_element_to_list(values)
    print("Caller, after:", values, "identity:", id(values))


if __name__ == "__main__":
    main()
