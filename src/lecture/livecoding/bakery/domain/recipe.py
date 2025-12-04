from lecture.livecoding.bakery.domain.bakery_object import BakeryObject
from lecture.livecoding.bakery.domain.bakery_product import Product, ProductType
from lecture.livecoding.bakery.repo.binary_file_repo import BinaryFileRepository


class Recipe(BakeryObject):
    def __init__(self, object_id: int, name: str, instructions: str, product: Product):
        super().__init__(object_id, name)
        self._instructions = instructions
        self._product = product

    @property
    def product(self):
        return self._product

    @property
    def instructions(self):
        return self._instructions

    def __str__(self):
        return f"Recipe <{self.name}> with id=<{self.id}> for {self.product} is: <{self.instructions}>"


if __name__ == "__main__":
    white_bread_1kg = Product(100, "Simple white bread", ProductType.BREAD)
    white_bread_recipe = Recipe(1000, "Simple white bread 1kg",
                                "1 kg white bread: mix 600 g flour, 360 ml warm water, 12 g salt, 7 g instant yeast, (optional 20 g sugar + 20 g oil/butter), knead 10 min, rise 60–90 min, shape, proof 30–45 min, bake 30–35 min at 220 °C, cool.",
                                white_bread_1kg)

    bagels_500g = Product(101, "Bagels 500g", ProductType.BAGEL)
    bagels_500g_recipe = Recipe(1001, "Bagels 500g recipe",
                                "Bagels: mix 500 g flour, 280 ml warm water, 7 g instant yeast, 10 g salt, 20 g sugar; knead 10 min; rise 60 min; divide + shape rings; rest 20 min; boil 1 min/side in water with 1 tbsp sugar; bake 20–22 min at 220 °C.",
                                bagels_500g)

    recipe_repo = BinaryFileRepository("recipes.bin")
    # recipe_repo.store(white_bread_recipe)
    # recipe_repo.store(bagels_500g_recipe)

    for r in recipe_repo:
        print(r.name)
        print(r.product)

    # print(white_bread_recipe)
    # print("-" * 20)
    # print(bagels_500g_recipe)
