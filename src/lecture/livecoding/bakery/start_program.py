"""
How to assemble the layered program
"""
from lecture.livecoding.bakery.repo.binary_file_repo import BinaryFileRepository
from lecture.livecoding.bakery.repo.abstract_text_file_repo import RecipeTextFileRepo

"""
    Initialize the repository layer
        - Each entity has its own repository
        - We can vary the type of repository (memory, file, etc.) by using different types
        - Read the properties file and create the correct repository type depending on it
"""

# we have the products
product_repo = BinaryFileRepository("products.bin")
# we need the product repo initialized so we can pass it to the recipes repository
recipe_repo = RecipeTextFileRepo("recipes.txt", product_repo)

"""
    Initialize the service layer
        - Repositories are provided as constructor parameters (called "dependency injection")
        - This allows us to change repository types without changing service code
        - Each entity has itw own service class (usually different entities do different things)
"""
product_service = ProductService(product_repo)
# perhaps the recipes service also needs access to products
recipe_service = RecipeService(recipe_repo, product_repo)

"""
    Initialize the presentation layer
        - There is only one UI class 
        - It has access to all service classes
        - If you want to implement GUI, you have 2 UI classes :) 
"""
bakery_ui = BakeryUI(product_service, recipe_service)
