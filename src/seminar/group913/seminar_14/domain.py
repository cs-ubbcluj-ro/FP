class Flight:
    def __init__(self, id, departure, departure_time, arrival, arrival_time):
        self.__id = id
        self.__departure = departure
        self.__arrival = arrival
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        
    @property
    def id(self):
        return self.__id
    
    @property
    def departure(self):
        return self.__departure
    
    @property
    def arrival(self):
        return self.__arrival
    
    @property
    def departure_time(self):
        return self.__departure_time
    
    @property
    def arrival_time(self):
        return self.__arrival_time
    
    def __str__(self):
        return self.__departure_time +  " | " + self.__arrival_time + " | " + self.__id + " | " + self.__departure + " - " +  self.__arrival
    
    def get_duration(self):
        return self.convert_time_to_minutes(self.__arrival_time) - self.convert_time_to_minutes(self.__departure_time)
        
    @staticmethod
    def convert_time_to_minutes(time):
        return int(time[:2]) * 60 + int(time[3:])
    
class Validator:
    @staticmethod
    def validate_time(time):
        '''
        validates a time from a string
        '''
        if len(time) != 5:
            raise ValueError("Invalid time") 
        if time[2] != ":":
            raise ValueError("Invalid time")
        hour = int(time[:2])
        minute = int(time[3:])
        if hour < 0 or hour > 23:
            raise ValueError("Invalid time")
        if minute < 0 or minute > 59:
            raise ValueError("Invalid time")   
        
    @staticmethod
    def validate_flight(flight):
        '''
        checks if the times are valid and the duration is between 15 and 90 minutes
        '''
        Validator.validate_time(flight.departure_time)
        Validator.validate_time(flight.arrival_time)
        
        if flight.get_duration() < 15 or flight.get_duration() > 90:
            raise ValueError("Invalid flight duration")