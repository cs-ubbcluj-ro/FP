from Seminar917.Seminar14.domain.validator import FlightValidator
from Seminar917.Seminar14.repository.textRepository import TextRepository
from Seminar917.Seminar14.service.flightService import FlightService
from Seminar917.Seminar14.ui.console import UI

if __name__=="__main__":
    flightRepository = TextRepository()
    flightValidator = FlightValidator()
    flightService = FlightService(flightRepository, flightValidator)

    ui = UI(flightService)
    ui.start()