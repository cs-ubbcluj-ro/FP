from domain import Flight, Validator

class ConsoleUI:
    def __init__(self, flight_services):
        self.__flight_services = flight_services
        
    def add_flight(self):
        id = input("id: ")
        departure = input("departure: ")
        departure_time = input("departure time: ")
        arrival = input("arrival: ")
        arrival_time = input("arrival time: ")
        flight = Flight(id, departure, departure_time, arrival, arrival_time)
        Validator.validate_flight(flight)
        self.__flight_services.add_flight(flight)
        
    
    def remove_flight(self):
        id = input("id: ")
        self.__flight_services.remove_flight(id)

    def print_all_flights(self):
        for flight in self.__flight_services.get_all_flights():
            print(flight)
            
    def print_airports(self):
        for airport in self.__flight_services.get_airports_by_traffic():
            print(airport)

    def print_intervals(self):
        for interval in self.__flight_services.get_free_time_intervals():
            print(interval)
            
    def print_disjoint_flights(self):
        for flight in self.__flight_services.get_maximum_disjoint_flights():
            print(flight)

    def run(self):
        commands = {
            "1": self.add_flight, 
            "2": self.remove_flight,
            "3": self.print_all_flights,
            "4": self.print_airports,
            "5": self.print_intervals,
            "6": self.print_disjoint_flights        
        }
        
        while True:
            print("1. Add flight")
            print("2. Remove flight")
            print("3. Print all flights")
            print("4. Print airports by traffic")
            print("5. Print free time intervals")
            print("6. Print disjoint flights")
            print("x. Exit")
            command = input(">>")
            if command == "x":
                break
            if command in commands:
                try:
                    commands[command]()
                except ValueError as ve:
                    print(ve)
            else:
                print("Invalid command")