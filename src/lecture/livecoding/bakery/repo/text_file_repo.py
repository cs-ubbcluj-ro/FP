from lecture.livecoding.bakery.repo.memory_repo import MemoryRepository


class RecipeTextFileRepo(MemoryRepository):
    """
    Repositories using text files are entity-specific, because each entity has different fields
    (attributes)

    Each Recipe is linked with exactly one Product
        -> when saving the Recipe to file, we save the (unique) id of the Product too
        -> when loading the Recipe from the file, we have the id of the Product, and can obtain the
        full object using the Product repository
    """

    def __init__(self, file_name: str, product_repo: MemoryRepository):
        super().__init__()
        self._file_name = file_name
        self._product_repo = product_repo

    def __load_file(self):
        """
        What to do here:
            1. Open the input file, read it line by line
            2. One of the tokens is the id of the related Product instance;
            retrieve the Product object calling self._product_repo.find(product_id)
            3. When creating the Recipe object,set the Product object in its constructor
        """
        pass
