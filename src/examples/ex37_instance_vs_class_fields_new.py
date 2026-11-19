"""
This example deliberately uses public attributes to focus on where state lives.
"""


class Student:
    # One class attribute
    count = 0

    def __init__(self, name="Anonymous"):
        self.name = name  # An instance attribute: each student has its own name.
        Student.count += 1

    @staticmethod
    def get_count():
        """Return class-level information; no individual student is needed."""
        return Student.count


def main():
    s1 = Student("Anna")
    s2 = Student("Carla")
    s1.name = "Alice"

    # Predict these results before running: Alice Carla, then 2 in a fresh run.
    print(s1.name, s2.name)
    print(Student.get_count())

    # Optional experiment: assigning s1.count creates an INSTANCE attribute,
    # which shadows the class attribute when accessed through s1.
    # s1.count = 99
    # print(s1.count, s2.count, Student.count)  # 99 2 2 in a fresh run.
    # This is why __init__ updates Student.count, not self.count.


if __name__ == "__main__":
    main()
