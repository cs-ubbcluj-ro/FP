class FlightApplicationException(Exception):
    pass

class RepoError(FlightApplicationException):
    pass

class ValidationError(FlightApplicationException):
    pass