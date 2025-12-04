from enum import Enum

from lecture.livecoding.bakery.domain.bakery_object import BakeryObject


class ProductType(Enum):
    BREAD = 1,
    CROISSANT = 2,
    BAGEL = 3,
    PASTRY = 4


class Product(BakeryObject):
    def __init__(self, object_id: int, name: str, product_type: ProductType):
        super().__init__(object_id, name)
        self._type = product_type

    @property
    def type(self):
        return self._type

    def __str__(self):
        return super().__str__() + " - " + str(self.type)


if __name__ == "__main__":
    br = Product(1000, "White bread", ProductType.BREAD)
    print(br)
