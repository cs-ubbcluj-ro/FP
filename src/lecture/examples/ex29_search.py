"""
Created on Dec 16, 2016

@author: Arthur
"""

'''
    1. Example of a class that overloads '==' operator.
    This allows using Python's inbuilt 'in' syntax
'''


class IDObject:
    """
    Base class that we use to demonstrate overloading '=='
    """

    def __init__(self, objectId):
        self._id = objectId

    @property
    def id(self):
        return self._id

    def __eq__(self, o):
        return type(o) == type(self) and o.id == self.id


'''
    2. We have a few derived classes
'''


class Car(IDObject):
    def __init__(self, carId, make, model):
        IDObject.__init__(self, carId)
        self._make = make
        self._model = model

    def __str__(self):
        return str(self.id) + " " + str(self._make) + " " + str(self._model)

    def __repr__(self):
        return str(self)


class Student(IDObject):
    def __init__(self, studentId, name):
        IDObject.__init__(self, studentId)
        self._name = name

    def __str__(self):
        return str(self.id) + " " + self._name

    def __repr__(self):
        return str(self)


'''
    3. Let's test how the '==' operator works
'''


def test_equals():
    c1 = Car(1, "Dacia", "Sandero")
    c2 = Car(1, "Dacia", "Logan")
    c3 = Car(2, "Dacia", "Lodgy")

    s1 = Student(1, "Anna")
    s2 = Student(1, "John")
    s3 = Student(2, "Maria")

    print(c1 == c1)
    print(s1 == s1)

    print(c1 == c2)
    print(c1 == c3)

    print(s1 == s2)
    print(s1 == s3)

    print(c1 == s1)
    print(c1 == s3)


'''
    4. Let's test how the 'in' operation works
'''


def test_in():
    c1 = Car(1, "Dacia", "Sandero")
    c2 = Car(1, "Dacia", "Logan")
    c3 = Car(2, "Dacia", "Lodgy")

    s1 = Student(1, "Anna")
    s2 = Student(1, "John")
    s3 = Student(2, "Maria")

    cars = [c1, c2, c3, s1]

    print(c1 in cars)
    print(s2 in cars)
    print(s3 in cars)


'''
    5. An example of an iterable collection that wraps a list
'''


class MyCollection:
    def __init__(self):
        self._data = []

    def add(self, o):
        self._data.append(o)

    def __iter__(self):
        """
        Return an iterator
        NB! This works only when a single iterator is requested at any one time
        """
        self._iterPoz = 0
        return self

    def __next__(self):
        """
        Returns the next element of the iteration
        """
        if self._iterPoz >= len(self._data):
            raise StopIteration()
        rez = self._data[self._iterPoz]
        self._iterPoz = self._iterPoz + 1
        return rez


def test_in_collection():
    c1 = Car(1, "Dacia", "Sandero")
    c2 = Car(2, "Dacia", "Logan")
    c3 = Car(3, "Dacia", "Lodgy")

    c4 = Car(4, "Dacia", "Duster")

    collection = MyCollection()
    collection.add(c1)
    collection.add(c2)
    collection.add(c3)

    '''
    This calls the __next__ method until StopIteration() is raised
    '''
    for c in collection:
        print(c)

    print(c3 in collection)
    print(c4 in collection)


test_in_collection()
