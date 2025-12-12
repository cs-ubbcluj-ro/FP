from lecture.livecoding.bakery.domain.bakery_object import BakeryObject
from lecture.livecoding.bakery.domain.ingredient import IngredientAmount, Units
from lecture.livecoding.bakery.domain.product import Product


class Recipe(BakeryObject):
    def __init__(self, object_id: int, name: str, ingredients: list[IngredientAmount], instructions: str,
                 product: Product, quantity: int, quantity_unit: Units):
        super().__init__(object_id, name)
        self._ingredients = ingredients
        self._instructions = instructions
        self._product = product
        self._quantity_value = quantity
        self._quantity_units = quantity_unit

    @property
    def product(self) -> Product:
        return self._product

    @property
    def ingredients(self) -> list[IngredientAmount]:
        # FIXME The list of ingredients can actually be modified via this property
        return self._ingredients

    @property
    def instructions(self) -> str:
        return self._instructions

    @property
    def quantity_value(self) -> int:
        return self._quantity_value

    @property
    def quantity_unit(self) -> Units:
        return self._quantity_units

    def __str__(self):
        result = f"Recipe - {self.id}, {self.name} with ingredients:\n"
        for ingr in self.ingredients:
            result += f"\tid {ingr.ingredient.id}, name {ingr.ingredient.name},quantity - {ingr.quantity} ({ingr.ingredient.unit.name}) \n"
        result += f"recipe will result in {self.quantity_value} {self.quantity_unit.name} of product {self.product}"
        return result
