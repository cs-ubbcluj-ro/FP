from Seminar917.Seminar14.domain.exceptions import FlightApplicationException
from Seminar917.Seminar14.service.flightService import FlightService
from Seminar917.Seminar14.domain.flight import Flight
from Seminar917.Seminar14.domain.myTime import MyTime

class UI:
    def __init__(self, flightService: FlightService):
        self.__service = flightService

    def printMenu(self):
        print("Flight menu:")
        print("1. Show flights")
        print("2. Add flight")
        print("3. Remove flight")
        print("4. List airports in decreasing order by activity")
        print("5. Longest no-fly time intervals")
        print("6. Flights allowed on backup radar")
        print("0. Exit")

    def printFlights(self):
        print("All flights")
        for flight in self.__service.getAll():
            print(flight)

    def __read_time(self, input_message):
        try:
            flight_dep_time = input(input_message)
            hour, minute = flight_dep_time.split(":")
            return MyTime(int(hour), int(minute))
        except ValueError:
            print("Incorrect string for time")
            return None

    def __readFlight(self) -> Flight:
        print("Adding a new flight")

        flight_id = ""
        while len(flight_id) < 1:
            flight_id = input("Id: ")

        flight_dep_city = ""
        while len(flight_dep_city) < 1:
            flight_dep_city = input("Departure city: ")

        flight_dep_time = None
        while flight_dep_time is None:
            flight_dep_time = self.__read_time("Departure time (hh:mm): ")

        flight_arr_city = ""
        while len(flight_arr_city) < 1:
            flight_arr_city = input("Arrival city: ")

        flight_arr_time = None
        while flight_arr_time is None:
            flight_arr_time = self.__read_time("Arrival time (hh:mm): ")

        return Flight(flight_id, flight_dep_city, flight_dep_time, flight_arr_city, flight_arr_time)

    def __addFlight(self):
        try:
            flight = self.__readFlight()
            self.__service.add(flight)
        except Exception as error:
            print(error)
            self.__addFlight()

    def start(self):
        while True:
            self.printMenu()

            try:
                choice = input("Your choice")
                if choice == "1":
                    self.printFlights()
                elif choice == "2":
                    self.__addFlight()
                elif choice == "0":
                    break
            except FlightApplicationException as fe:
                print(fe)
