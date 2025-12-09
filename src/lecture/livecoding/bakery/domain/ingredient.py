from enum import Enum

from lecture.livecoding.bakery.domain.bakery_object import BakeryObject


class Units(Enum):
    MILLILITER = 1,
    GRAM = 2,
    SPOONFUL = 3


class Ingredient(BakeryObject):
    def __init__(self, object_id: int, name: str, measurement_unit: Units):
        super().__init__(object_id, name)
        self._unit = measurement_unit

    @property
    def unit(self) -> Units:
        return self._unit

    def __str__(self):
        return f"Ingredient - {self.id}, {self.name}, unit {self.unit}"


class IngredientAmount:
    def __init__(self, ingredient: Ingredient, quantity: int):
        self._ingredient = ingredient
        self._quantity = quantity

    @property
    def ingredient(self) -> Ingredient:
        return self._ingredient

    @property
    def quantity(self) -> int:
        return self._quantity

    def __str__(self):
        return f"<({self.ingredient.id},{self.ingredient.name}),{self.quantity}>"

    def __repr__(self):
        return str(self)
