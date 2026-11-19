"""Instances, dynamic attributes, self and Python's naming conventions.

Author: Arthur
"""


class FirstClass:
    pass


class SecondClass:
    def __init__(self):
        # Initialize the expected attributes so each instance starts predictably.
        self.test_one = "Test One"
        self._test_two = "Test Two"
        self.__test_three = "Test Three"

    def get_public_value(self):
        """Return the value stored in this instance's public attribute."""
        return self.test_one


def main():
    x = FirstClass()
    print(type(x))

    # Ordinary Python instances can acquire attributes dynamically.
    # In our application classes we normally initialize them in __init__.
    x.name = "Alice"
    x.salary = 100
    x.salary += 20
    y = FirstClass()
    y.name = "Bob"
    y.salary = 1000
    print("Name and salary of x:", x.name, x.salary)
    print("Name and salary of y:", y.name, y.salary)

    y.hello = "Say hello"
    print(y.hello)
    # Predict what happens if you uncomment this line: x has no hello attribute.
    # print(x.hello)

    obj = SecondClass()
    print(obj.test_one)
    # These calls use the same function with the same instance as self.
    print(obj.get_public_value())
    print(SecondClass.get_public_value(obj))

    # _test_two is non-public by convention, but access is technically possible.
    # Uncomment for demonstration only; client code should respect the interface.
    # print(obj._test_two)

    # __test_three is name-mangled, not protected by an access restriction.
    # print(obj.__test_three)              # Raises AttributeError.
    # print(obj._SecondClass__test_three)  # Works, but bypasses the interface.


if __name__ == "__main__":
    main()
