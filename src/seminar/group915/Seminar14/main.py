from Seminar915.Seminar14.domain.validator import FlightValidator
from Seminar915.Seminar14.repository.textRepository import FlightRepository
from Seminar915.Seminar14.service.flightService import FlightService
from Seminar915.Seminar14.ui.console import UI

if __name__=="__main__":
    flightRepository = FlightRepository()
    flightValidator = FlightValidator()
    flightService = FlightService(flightRepository, flightValidator)

    ui = UI(flightService)
    ui.start()