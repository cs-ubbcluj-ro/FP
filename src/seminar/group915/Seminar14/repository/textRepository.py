from Seminar915.Seminar14.domain.myTime import MyTime
from Seminar915.Seminar14.domain.flight import Flight

class RepoError(Exception):
    pass

class FlightRepository:
    def __init__(self, filename = "flights.txt"):
        self.__filename = filename
        self.__data = {}
        self.__loadData()

    def add(self, flight: Flight):
        if flight.identifier in self.__data.keys():
            raise RepoError("Flight already exists")

        self.__data[flight.identifier] = flight
        self.__saveFile()


    def __loadData(self):
        lines = []

        try:
            fin = open(self.__filename, "rt")
            lines = fin.readlines()
            fin.close()
        except:
            raise RepoError("Something went wrong")

        for line in lines:
            currentLine = line.split(",")
            time = currentLine[2].split(":")
            departureTime = MyTime(int(time[0]), int(time[1]))
            time = currentLine[4].split(":")
            arrivalTime = MyTime(int(time[0]), int(time[1]))
            newFlight = Flight(currentLine[0], currentLine[1], departureTime, currentLine[3], arrivalTime)
            self.__data[newFlight.identifier] = newFlight

    def getAll(self):
        return self.__data.values()

    def __saveFile(self):
        fout = open(self.__filename, "wt")
        flights = self.getAll()
        for flight in flights:
            flightString = flight.identifier + "," + flight.departureCity + "," + str(flight.departureTime) + "," + flight.arrivalCity + "," + str(flight.arrivalTime) + "\n"
            fout.write(flightString)

        fout.close()
