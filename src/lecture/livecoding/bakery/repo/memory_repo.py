from lecture.livecoding.bakery.domain.bakery_object import BakeryObject
from lecture.livecoding.bakery.domain.product import Product


class BakeryError(Exception):
    pass


class DuplicateIDError(BakeryError):
    pass


class RepositoryIterator:
    def __init__(self, elements):
        self._elements = list(elements)  # make a list of all elements
        self.__pos = -1  # we start before the first element in the list

    def __next__(self):
        """
        Returns the current element and moves to the next element, as long as it exsits
        """
        self.__pos += 1
        if self.__pos == len(self._elements):
            # signal that we have run out of elements to iterate over
            raise StopIteration()

        return self._elements[self.__pos]


class MemoryRepository:
    def __init__(self):
        self._data = {}

    def store(self, element: BakeryObject):
        if element.id in self._data:
            # Signal that we have a problem
            raise DuplicateIDError("Duplicate ID")
        self._data[element.id] = element

    def remove(self, element: BakeryObject):
        pass

    def find(self, element_id: int) -> BakeryObject:
        if element_id not in self._data:
            raise BakeryError(f"Element with id - {element_id} not found in repository")
        return self._data[element_id]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        """
        Methods returns an iterator over the repository

        What is a iterator?
            - a way to visit each element of a data structure, so that no elements are left out, and each element is
            visited only once
            - Iterator is a design pattern
            https://refactoring.guru/design-patterns/iterator
        """
        return RepositoryIterator(self._data.values())
