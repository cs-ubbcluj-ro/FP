from enum import Enum

from lecture.livecoding.bakery.domain.bakery_object import BakeryObject


class ProductType(Enum):
    BREAD = 1,
    PASTRY = 2,
    PANCAKES = 3


class Product(BakeryObject):
    def __init__(self, object_id: int, name: str, product_type: ProductType):
        super().__init__(object_id, name)
        self._type = product_type

    @property
    def type(self):
        return self._type

    def __str__(self):
        return f"Product - {self.id}, {self.name}, type {self.type}"
