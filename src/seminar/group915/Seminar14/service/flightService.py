from Seminar915.Seminar14.domain.flight import Flight
from Seminar915.Seminar14.domain.validator import FlightValidator
from Seminar915.Seminar14.repository.textRepository import FlightRepository


class FlightService:
    def __init__(self, flightRepository: FlightRepository, validator: FlightValidator):
        self.__repository = flightRepository
        self.__validator = validator

    def add(self, flight: Flight):
        self.__validator.validate(flight)
        self.__repository.add(flight)

    def getAll(self):
        return self.__repository.getAll()