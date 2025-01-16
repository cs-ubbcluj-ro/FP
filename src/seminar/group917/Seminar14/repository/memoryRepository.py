from Seminar917.Seminar14.domain.exceptions import RepoError
from Seminar917.Seminar14.domain.flight import Flight

class MemoryRepository:
    def __init__(self):
        self._data = {}

    def add(self, flight: Flight):
        if flight.identifier in self._data.keys():
            raise RepoError("Flight already exists")

        self._data[flight.identifier] = flight

    def remove(self, identifier: str) -> Flight:
        if identifier not in self._data.keys():
            raise RepoError("Flight does not exist")
        return self._data.pop(identifier)

    def getAll(self):
        return self._data.values()