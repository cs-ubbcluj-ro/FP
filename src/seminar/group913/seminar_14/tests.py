import unittest
import os 

from repository import FlightRepo
from services import FlightServices
from domain import Flight

class Tests(unittest.TestCase):
    def test_add_flight(self):
        '''
        tetst the add_flight method from the services
        '''
        test_file_path = os.path.join(os.path.dirname(__file__), "test_flights.txt")   
        repo = FlightRepo(test_file_path)     
        services = FlightServices(repo)
        services.add_flight(Flight("1", "a", "10:00", "b", "10:45"))
        self.assertEqual(len(services.get_all_flights()), 1)
        services.add_flight(Flight("2", "b", "12:20", "c", "12:40"))
        self.assertEqual(len(services.get_all_flights()), 2)
        try:
            services.add_flight(Flight("1", "c", "10:50", "d", "10:60"))
            assert False
        except ValueError:
            assert True
            
        try:
            services.add_flight(Flight("3", "a", "10:00", "b", "10:05"))
            assert False 
        except ValueError:
            assert True
        self.assertEqual(len(services.get_all_flights()), 2)