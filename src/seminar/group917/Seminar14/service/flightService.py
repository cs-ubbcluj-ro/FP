from Seminar917.Seminar14.domain.flight import Flight
from Seminar917.Seminar14.domain.validator import FlightValidator
from Seminar917.Seminar14.repository.textRepository import TextRepository


class FlightService:
    def __init__(self, flightRepository: TextRepository, flightvalidator: FlightValidator):
        self.__repository = flightRepository
        self.__validator = flightvalidator

    def add(self, flight: Flight):
        self.__validator.validate(flight)
        self.__repository.add(flight)

    def remove(self, identifier: str) -> Flight:
        return self.__repository.remove(identifier)

    def getAll(self):
        return self.__repository.getAll()