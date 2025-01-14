from Seminar916.Seminar14.domain.validator import FlightValidator
from Seminar916.Seminar14.repository.textRepository import TextRepository


class FlightService:
    def __init__(self, flightRepository: TextRepository, flightvalidator: FlightValidator):
        self.__repository = flightRepository
        self.__validator = flightvalidator

    def add(self, flight):
        self.__validator.validate(flight)
        self.__repository.add(flight)

    def remove(self, identifier):
        self.__repository.remove(identifier)

    def getAll(self):
        return self.__repository.getAll()