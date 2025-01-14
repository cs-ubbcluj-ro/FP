from Seminar915.Seminar14.domain.flight import Flight

class ValidationError(Exception):
    pass

class FlightValidator:
    def validate(self, flight: Flight):
        errors = []

        if flight.departureCity == flight.arrivalCity:
            errors.append("Flight should arrive at different airport")
        if flight.departureTime > flight.arrivalTime:
            errors.append("Flight should depart before arrival")
        elif not 15 <= flight.arrivalTime - flight.departureTime <= 90:
            errors.append("Flights must be between 15 and 90 minutes!")
        if len(errors) > 0:
            raise ValidationError(errors)