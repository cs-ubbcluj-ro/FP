"""
What does the exam day look like? Let's say exam starts at 09:00

    1. Written test 09:00 - 10:30
        (what a piece of code does, O(n), problem solving methods, etc)
    2. Break 10:30 - 12:00 ?
    3. Practical test 12:00 - 14:45
        (have to implement a Python 3 program using classes, objects, layered architecture)
        (work on your own laptop, own IDE, using a GitHub assignment)
        (we only grade functionalities that work through the UI)
    4. 14:45 - 15:45 - grading the practical test
    5. Check the result of the written test & final grade @ FP (before 16:00)
    6. Exit

"""

"""
    Algorithm Complexity
"""


# 1
# T(n) = log_3(n) => O(n) belongs to log_3(n)

# 3
# recurrence is
# T(n) = 4 * T(n/2) + 1
# T(1) = 1


# T(n) = 4 * T(n/2) + 1 = 4 * [ 4 * T(n/4) + 1 ] + 1 =
# T(n/2) = 4 * T(n/4) + 1
# T(n/4) = 4 * T(n/8) + 1
#
# T(n) = 4 * [ 4 * [ 4 * T(n/8) + 1 ] + 1 ] + 1

# a number k must exist so that k = log_2(n), or 2^k = n

# T(n) = 4^3 * T(n/8) + 64 + 16 + 4 + 1
# T(n) = (4^k) * T(n/2^k) + 4^k + 4^(k-1) + ... + 4 + 1
# T(n) = n^2 * 1 + (n^2 + 1) / 3 => O(n^2)


class MyIterator:
    def __init__(self, elements):
        self.__elements = elements
        self.__pos = -1

    def __next__(self):
        self.__pos += 1
        if self.__pos >= len(self.__elements):
            # Tell the for loop there are no more elements :(
            raise StopIteration()

        return self.__elements[self.__pos]


class MyIterableStructure:

    def __init__(self):
        self.__data = []

    def add(self, elem: object):
        self.__data.append(elem)

    def __iter__(self):
        """
        To iterate a collection = go over every element of the collection exactly once
        :return:
        """
        # TODO maybe create a copy of the data so we don't break the actual list
        return MyIterator(self.__data)


struct = MyIterableStructure()
for i in range(10):
    struct.add(i)

for elem in struct:  # iterates over the collection
    print(elem)
