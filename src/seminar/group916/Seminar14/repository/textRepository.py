from Seminar916.Seminar14.repository.memoryRepository import MemoryRepository
from Seminar916.Seminar14.domain.exceptions import RepoError
from Seminar916.Seminar14.domain.myTime import MyTime
from Seminar916.Seminar14.domain.flight import Flight

class TextRepository(MemoryRepository):
    def __init__(self, filename = "flights.txt"):
        super().__init__()
        self.__filename = filename
        self.__loadFile()

    def __loadFile(self):
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
            super().add(newFlight)

    def __saveFile(self):
        fout = open(self.__filename, "wt")
        flights = super().getAll()
        for flight in flights:
            flightString = flight.identifier + "," + flight.departureCity + "," + str(
                flight.departureTime) + "," + flight.arrivalCity + "," + str(flight.arrivalTime) + "\n"
            fout.write(flightString)

        fout.close()

    def add(self, flight: Flight):
        super().add(flight)
        self.__saveFile()

    def remove(self, identifier: str) -> Flight:
        flightToBeRemoved = super().remove(identifier)
        self.__saveFile()
        return flightToBeRemoved


