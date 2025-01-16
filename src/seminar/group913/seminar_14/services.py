from domain import Flight


class FlightServices:
    def __init__(self, flight_repo):
        self.__flight_repo = flight_repo

    def add_flight(self, flight):
        '''
        adds a flight to the repository
        :param: flight - the flight
        :raise: ValueError if the airport is busy
        '''
        if self.is_airport_busy(flight.departure, flight.departure_time) or self.is_airport_busy(flight.arrival,
                                                                                                 flight.arrival_time):
            raise ValueError("Airport is busy")
        self.__flight_repo.add(flight)

    def remove_flight(self, id):
        self.__flight_repo.remove(id)

    def is_airport_busy(self, airport, time):
        '''
        checks if an airport is busy at a certain time
        :param: airport - the airport to check
        :param: time - the time to check
        :return: True if the airport is busy, False otherwise
        '''
        for flight in self.__flight_repo.get_all():
            if flight.departure == airport and flight.departure_time == time:
                return True
        return False

    def get_airports_by_traffic(self):
        '''
        returns a list of airports sorted by traffic
        :return: a list of airports sorted by traffic
        '''
        airports = {}
        for flight in self.__flight_repo.get_all():
            if flight.departure not in airports:
                airports[flight.departure] = 1
            else:
                airports[flight.departure] += 1
            if flight.arrival not in airports:
                airports[flight.arrival] = 1
            else:
                airports[flight.arrival] += 1

        return sorted(airports, key=airports.get, reverse=True)

    def get_all_flights(self):
        return self.__flight_repo.get_all()

    def get_free_time_intervals(self):
        events = []
        free_intervals = []
        for flight in self.__flight_repo.get_all():
            events.append((flight.departure_time, 1))
            events.append((flight.arrival_time, -1))
        events.sort()

        planes_in_air = 0
        for i in range(1, len(events)):
            if planes_in_air == 0:
                if i > 1:
                    free_intervals.append((events[i - 1][0], events[i][0]))
                else:
                    free_intervals.append(("00:00", events[i][0]))
            planes_in_air += events[i][1]

        if planes_in_air == 0:
            free_intervals.append((events[-1][0], "23:59"))

        free_intervals.sort(reverse=True,
                            key=lambda x: Flight.convert_time_to_minutes(x[1]) - Flight.convert_time_to_minutes(x[0]))
        return free_intervals

    def get_maximum_disjoint_flights(self):
        flights = list(self.__flight_repo.get_all())
        flights.sort(key=lambda x: x.arrival_time)
        last_flights = [flights[0]]
        for flight in flights:
            if flight.departure_time >= last_flights[-1].arrival_time:
                last_flights.append(flight)

        return last_flights
