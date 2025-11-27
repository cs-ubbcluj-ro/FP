"""
Simplest class that we can write in Python
What is a class?
    - A class is a definition for a data type
    - It's a template, or blueprint, plan used to create objects
    - A class is a collection of state (fields, variables) and
    behaviour (functions, methods)
"""


class Rational:
    """
    This variable belongs to the class itself, and not any of its objects
    This means we can access it without refering to "self"
    """
    _number_of_instances = 0

    def __init__(self, numerator: int, denominator: int = 1):
        """
        :param numerator: Numerator
        :param denominator: Denominator (default value 1, cannot be 0)

        Details
            - __init__ is the constructor for class Rational
            - Returns a new rational number
            - NB! The constructor implicitly returns a reference to the newly
            created object -- you should not write a return here
        """

        # These attributes are public (accessible from anywhere)
        # self.numerator = numerator
        # self.denominator = denominator

        # These attributes are private
        # In Python, this is by convention (you should not modify them
        # from outside the class)
        self._numerator = numerator
        self._denominator = denominator

        # These attributes are (still) private
        # In Python, this is enforced by name mangling (the field or
        # method names are changed internally)
        # self.__numerator = numerator
        # self.__denominator = denominator

        # TODO call gcd() to simplify the fraction
        if denominator == 0:
            raise ValueError("Cannot have 0 denominator")

        Rational._number_of_instances += 1

    @staticmethod
    def get_number_of_instance():
        return Rational._number_of_instances

    @property
    def numerator(self):
        """
        Properties combine the best things about accessing fields and
        having getter/setter methods
        """
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError("Cannot have 0 denominator")
        self._denominator = value

    def set_numerator(self, new_value: int):
        self._numerator = new_value

    def get_numerator(self):
        # inside class methods we can access and change private
        # things
        return self._numerator

    def to_str(self) -> str:
        return str(self.numerator) + "/" + str(self.denominator)

    def add(self, q):
        # Returns self + q
        new_numerator = self.numerator * q.denominator + self.denominator * q.numerator
        new_denominator = self.denominator * q.denominator
        return Rational(new_numerator, new_denominator)

    def __add__(self, other):
        return self.add(other)

    def __str__(self):
        # TODO Don't display 5/1 but 5 ,...
        # This is the Python way
        # Represent the self object as a Python str
        return str(self.numerator) + "/" + str(self.denominator)

if __name__ == "__main__":
    # q is an object of type Rational
    q = Rational(5, 2)
    print(type(q))
    print(q.set_numerator(3))

    # How to access Python class methods
    print(q.get_numerator())
    # another way
    print(Rational.get_numerator(q))  # we assume q is Rational

    # this is ok, but a bit too verbose
    q.set_numerator(q.get_numerator() + 1)

    q.numerator += 1
    q.denominator -= 1
    # q.denominator -= 1  # should be 0
    # print(q.numerator)

    q2 = q.add(Rational(7, 2))

    q_final = q2 + q + q2 + q + q2 + q + q + q + q + q

    print(q + Rational(7, 2))
    print(q2)
    print(q_final)

    print(Rational.get_number_of_instance())
    q0 = None
    try:
        """
        1. Call to Rational class constructor
            -> raises an exception => steps 2, 3 no longer take place
        2. Type of Rational object transfered to q0
        3. Value of Rational object transfered to q0
        """
        q0 = Rational(1, 0)
    except ValueError as ve:
        print(ve)
        print(q0)
    print(Rational.get_number_of_instance())  # ??

    # q.denominator = 0  # no bueno
