from lecture.livecoding.bakery.domain.product import ProductType, Product
from lecture.livecoding.bakery.repo.abstract_text_file_repo import AbstractTextFileRepo


class ProductTextFileRepo(AbstractTextFileRepo):
    def __init__(self, file_name: str):
        super().__init__(file_name)

    def _save_file(self):
        # TODO Implement me ...
        pass

    def _load_file(self):
        fin = open(self._file_name, "rt")
        lines = fin.readlines()
        fin.close()

        for line in lines:
            tokens = line.split(",")
            _id = int(tokens[0].strip())
            _name = tokens[1].strip()
            _product_type = tokens[2].strip()
            self.store(Product(_id, _name, ProductType[_product_type]))


if __name__ == "__main__":
    repo = ProductTextFileRepo("../products.txt")
    for ingredient in repo:
        print(ingredient)