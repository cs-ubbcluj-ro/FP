from domain import Flight

class FlightRepo:
    def __init__(self, filename="flights.txt"):
        self.__flights = {}
        self.__filename = filename
        self.__load() 
        
    def __load(self):
        try:
            with open(self.__filename, "r") as f:
                for line in f:
                    flight = line.strip().split(",")
                    self.__flights[flight[0]] = Flight(flight[0], flight[1], flight[2], flight[3], flight[4])
        except FileNotFoundError:
            raise ValueError("File not found")
        
    def __save(self):
        with open(self.__filename, "w") as f:
            for flight in self.__flights.values():
                f.write(str(flight.id) + "," + str(flight.departure) + "," + str(flight.departure_time) + "," + str(flight.arrival) + "," + str(flight.arrival_time) + "\n")
        
    def get_all(self):
        return self.__flights.values()
    
    def add(self, obj):
        if obj.id in self.__flights:
            raise ValueError("Flight already exists")
        self.__flights[obj.id] = obj
        self.__save()
    
    def remove(self, id):
        if id not in self.__flights:
            raise ValueError("Flight does not exist")
        del self.__flights[id]
        self.__save()
    
        