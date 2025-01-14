from datetime import time

class Flight:
    def __init__(self, identifier: str, departureCity: str, departureTime: time, arrivalCity: str, arrivalTime: time):
        if not isinstance(identifier, str):
            raise TypeError("Identifier should be a string")
        if not isinstance(departureTime, time):
            raise TypeError("Departure time should be a time instance")

        self.__identifier = identifier
        self.__departureCity = departureCity
        self.__departureTime = departureTime
        self.__arrivalCity = arrivalCity
        self.__arrivalTime = arrivalTime

    @property
    def identifier(self):
        return self.__identifier

    @property
    def departureTime(self):
        return self.__departureTime

    @property
    def departureCity(self):
        return self.__departureCity

    @property
    def arrivalCity(self):
        return self.__arrivalCity

    @property
    def arrivalTime(self):
        return self.__arrivalTime

    def __str__(self):
        return "Flight " + self.identifier + " departs from " + self.departureCity + " at " + str(
            self.departureTime) + ", arrives at " + self.arrivalCity + " at " + str(self.arrivalTime)
