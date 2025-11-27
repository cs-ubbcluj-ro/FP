"""
    We have no slides for today :(

    What we cover today
        1. Inheritance (one of the pillars of object oriented programming)
        2. The Repository layer of the application
        3. Working with files! yay!

    Pillars of object oriented programming
        1. Encapsulation (bundling state and bahaviour together and selecting
        what to expose to the outside world)

        2. Inheritance (reuse code, specialize code, allow us to change things
        further down the line)

        3. Polymorphism (changing the way objects react to messages)
"""


class A(object):
    """
    object is a built-in Python class
    object is the root of the Python inheritance tree
    class A inherits from class object
        - All Python classes (except object) inherit from object (either directly or
        transitively)
        what does this actually mean?
            - All non-private fields and methods of class object also appear in class A

    """

    def __init__(self):
        self.__a = 10

    def m(self):
        return "A"


class B(A):
    """
    class B inherits from class A which inherits from class object
    class B is a descendant of object

    """

    def __init__(self):
        # We should call the constructor of the base class in Python
        super().__init__()

    def m(self):
        """
        Overrides method m() from class A
        """
        # x = self.m()
        # A.m(self)
        print(super().m())

        return "B"


a = A()
print(str(a))
print(a.__str__())
print(a.m())

b = B()
print(b.__str__())
print(b.m())

# print(b.m())
# b = A()
# print(b.m())
# b = B()
# print(b.m())
