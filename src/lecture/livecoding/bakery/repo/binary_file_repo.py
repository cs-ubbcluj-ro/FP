import pickle

from lecture.livecoding.bakery.domain.bakery_object import BakeryObject
from lecture.livecoding.bakery.domain.bakery_product import Product
from lecture.livecoding.bakery.repo.memory_repo import MemoryRepository


class BinaryFileRepository(MemoryRepository):
    def __init__(self, file_name: str = "products.bin"):
        super().__init__()  # call to super constructor should be the first line in the method
        self._file_name = file_name

        try:
            self.__load_file()
        except FileNotFoundError:
            # We assume we start from an empty repo
            print("Starting from an empty repo")

    def store(self, product: BakeryObject):
        # We override store to make sure the new Product is also saved into the file :)
        super().store(product)
        """
        In case calling super().store(product) resulted in a DuplicateIDError, the line below does not run; the method
        exits with an Exception that is propagated to whoever called the function
        """
        self.__save_file()

    def __save_file(self):
        fout = open(self._file_name, "wb")
        pickle.dump(self._data, fout)
        fout.close()

    def __load_file(self):
        fin = open(self._file_name, "rb")
        self._data = pickle.load(fin)
        fin.close()


if __name__ == "__main__":
    # repo = MemoryRepository()
    # repo.store(Product(1000, "White bread", ProductType.BREAD))
    # repo.store(Product(1001, "Black bread", ProductType.BREAD))
    # repo.store(Product(1002, "Pretzel", ProductType.BAGEL))
    # print(len(repo))

    bin_repo = BinaryFileRepository()
    for p in bin_repo:
        print(p)

    # bin_repo.store(Product(1000, "A", ProductType.CROISSANT))

    # for product in repo:
    #     bin_repo.store(product)
    #
    # bin_repo.save_file()
