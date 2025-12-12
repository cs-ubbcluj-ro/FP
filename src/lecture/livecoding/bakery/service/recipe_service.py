from lecture.livecoding.bakery.domain.ingredient import Ingredient
from lecture.livecoding.bakery.domain.recipe import Recipe
from lecture.livecoding.bakery.repo.ingredient_text_file_repo import IngredientTextFileRepo
from lecture.livecoding.bakery.repo.memory_repo import MemoryRepository
from lecture.livecoding.bakery.repo.product_text_file_repo import ProductTextFileRepo
from lecture.livecoding.bakery.repo.recipe_text_file_repo import RecipeTextFileRepo


class ProductSaltContentDTO:
    def __init__(self, recipe: Recipe, salt_content: float):
        self.__recipe = recipe
        self.__salt_content = salt_content

    @property
    def recipe(self):
        return self.__recipe

    @property
    def salt_content(self):
        return self.__salt_content

    def __lt__(self, other):
        return self.salt_content < other.salt_content


class RecipeService:
    def __init__(self, ingredients_repo: MemoryRepository, recipes_repo: MemoryRepository):
        self._recipes_repo = recipes_repo
        self._ingredients_repo = ingredients_repo

    def low_salt_recipes(self, salt: Ingredient) -> list[ProductSaltContentDTO]:
        result_list = []

        for recipe in self._recipes_repo:
            total_salt = 0
            for ingredient_amount in recipe.ingredients:
                if salt.id == ingredient_amount.ingredient.id:
                    total_salt += ingredient_amount.quantity

            """
            Calculate the salt content per 100g of product
            """
            total_quantity = recipe.quantity_value
            result_list.append(ProductSaltContentDTO(recipe, total_salt * (100 / total_quantity)))
            """
            lambdas are anonymous functions => lambdas are called exactly where they are defined
            """
            result_list.sort(key=lambda x: x.salt_content)

        # print(result_list)
        return result_list


if __name__ == "__main__":
    ingredients_repo = IngredientTextFileRepo("../ingredients.txt")
    product_repo = ProductTextFileRepo("../products.txt")
    """
    For layered architecture !!
        - Transmit the repositories as constructor parameters, as this allows us to change the type of repository we use
        without changing the service class source code
        - Early form of "dependency injection"
    """
    recipes_repo = RecipeTextFileRepo("../recipes.txt", product_repo, ingredients_repo)

    recipes_service = RecipeService(ingredients_repo, recipes_repo)
    low_salt_recipes = recipes_service.low_salt_recipes(ingredients_repo.find(306))

    for recipes_dto in low_salt_recipes:
        print(recipes_dto.salt_content, recipes_dto.recipe.quantity_value, recipes_dto.recipe.name)
