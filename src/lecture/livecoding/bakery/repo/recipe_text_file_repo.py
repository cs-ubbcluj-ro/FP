from lecture.livecoding.bakery.domain.ingredient import IngredientAmount, Units
from lecture.livecoding.bakery.domain.recipe import Recipe
from lecture.livecoding.bakery.repo.abstract_text_file_repo import AbstractTextFileRepo
from lecture.livecoding.bakery.repo.ingredient_text_file_repo import IngredientTextFileRepo
from lecture.livecoding.bakery.repo.memory_repo import MemoryRepository
from lecture.livecoding.bakery.repo.product_text_file_repo import ProductTextFileRepo


class RecipeTextFileRepo(AbstractTextFileRepo):
    def __init__(self, file_name: str, product_repo: MemoryRepository, ingredient_repo: MemoryRepository):
        self._product_repo = product_repo
        self._ingredient_repo = ingredient_repo
        super().__init__(file_name)

    def _load_file(self):
        fin = open(self._file_name, "rt")
        lines = fin.readlines()
        fin.close()

        for line in lines:
            tokens = line.split(",")
            _id = int(tokens[0].strip())
            _name = tokens[1].strip()

            _product_id = int(tokens[2].strip())
            product = self._product_repo.find(_product_id)

            _quantity_value = int(tokens[3].strip())
            _quantity_unit = Units[tokens[4].strip()]

            ingredient_amount_list = []
            for index in range(5, len(tokens), 2):
                ingredient_id = int(tokens[index].strip())
                ingredient = self._ingredient_repo.find(ingredient_id)
                ingredient_amount = int(tokens[index + 1].strip())
                ingredient_amount_list.append(IngredientAmount(ingredient, ingredient_amount))

            self.store(Recipe(_id, _name, ingredient_amount_list, "n/a", product, _quantity_value, _quantity_unit))


if __name__ == "__main__":
    ingredients_repo = IngredientTextFileRepo("../ingredients.txt")
    product_repo = ProductTextFileRepo("../products.txt")

    recipes_repo = RecipeTextFileRepo("../recipes.txt", product_repo, ingredients_repo)
    print(len(recipes_repo))
    for recipe in recipes_repo:
        print(recipe)
        print("-" * 50)
