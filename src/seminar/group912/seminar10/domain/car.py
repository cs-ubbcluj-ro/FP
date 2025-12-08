from enum import Enum

from seminar.group912.seminar10.domain.id_entity import IDEntity


class CarColors(Enum):
    BLACK = 1
    RED = 2
    GREEN = 3
    YELLOW = 4
    BLUE = 5
    MAGENTA = 6
    CYAN = 7


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

    def __init__(self, car_id: int, license_plate: str, model: str, color: CarColors):
        super().__init__(car_id)
        self._license_plate = license_plate
        self._model = model
        self._color = color

    @property
    def license_plate(self) -> str:
        return self._license_plate

    @property
    def model(self) -> str:
        return self._model

    @property
    def color(self) -> Enum:
        return self._color
