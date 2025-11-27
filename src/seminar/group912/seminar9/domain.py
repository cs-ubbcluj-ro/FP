"""
We start work on a multi-week problem statement.
    - We'll have several entities in the problem domain
    - We'll use several repository types
"""
from enum import Enum


class IDEntity(object):
    """
    Class will have:
        1. constructor that takes an id parameter of type int
        2. a property called id that is
            - read-only
            - an int
            - returns the id assigned via the constructor
    """
    pass


class CarColors(Enum):
    BLACK = 1  # add more colors


class Car(IDEntity):
    """
    Class will have:
        - license plate : str
        - model : str (e.g., "VW Polo")
        - color : Enum (create an Enum called CarColor with several colors)

    Create the following attributes:
        - license plate : str
        - model : str (e.g., "VW Polo")
        - color : Enum
    All attributes are read-only (only @property)
    """

    def __init__(self, car_id: int, license: str, model: str, color: CarColors):
        pass
