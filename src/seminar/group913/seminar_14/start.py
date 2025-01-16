from repository import FlightRepo
from services import FlightServices
from ui import ConsoleUI

def main():
    repo = FlightRepo("flights.txt")
    services = FlightServices(repo)
    ui = ConsoleUI(services)
    ui.run() 
    
main()