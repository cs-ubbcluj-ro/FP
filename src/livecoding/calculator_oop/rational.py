class Rational:
    __rational_count = 0

    def __init__(self, numerator: int = 0, denominator: int = 1):
        """
        public - name does not start with _, it can be accessed from anywhere
        private - name starts with _ or __ - it can only be accessed from inside the class

        __ results in name mangling (Python interpreter renames the field in a predictable way)
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        self.__numerator = numerator
        self.__denominator = denominator
        Rational.__rational_count += 1

    # This means the method is linked to the class itself, and not any object
    @staticmethod
    def get_number_of_objects():
        return Rational.__rational_count

    def get_numerator(self) -> int:
        return self.__numerator

    def get_denominator(self) -> int:
        return self.__denominator

    def add(self, q):
        new_num = self.__numerator * q.__denominator + self.__denominator * q.__numerator
        new_den = self.__denominator * q.__denominator
        return Rational(new_num, new_den)

    def __add__(self, other):
        return self.add(other)

    def __str__(self):
        return f"{self.get_numerator()}/{self.get_denominator()}"

    # def set_denominator(self, new_value):
    #     if new_value == 0:
    #         raise ValueError("Denominator cannot be 0")
    #     self.__denominator = new_value


"""
Rational is a class - a template for the new data type
q is an object - it is an instance of class Rational
"""
print("count= ", Rational.get_number_of_objects())

q1 = Rational(1, 2)

# print(q.__numerator, q.__denominator)

q2 = Rational(2, 5)
# print(q2.numerator, q2.denominator)


q3 = q1.add(q2)
q3 = Rational.add(q1, q2)

q3 = q1 + q2

print(q3)
print(type(q3))

# print(q2.__numerator)
# print(q2.get_numerator())
# print(Rational.get_numerator(q2))

print("count= ", Rational.get_number_of_objects())

# print(id(q))
# print(type(q))
