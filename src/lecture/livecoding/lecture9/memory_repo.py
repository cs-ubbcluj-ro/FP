import pickle

from lecture.livecoding.lecture9.bakery_product import Product, ProductType


class BakeryError(Exception):
    pass


class DuplicateIDError(BakeryError):
    pass


class RepositoryIterator:
    def __init__(self, elements):
        self._elements = list(elements)  # make a list of all elements
        self.__pos = -1  # we start before the first element in the list

    def __next__(self):
        """
        Returns the current element and moves to the next element, as long as it exsits
        """
        self.__pos += 1
        if self.__pos == len(self._elements):
            # signal that we have run out of elements to iterate over
            raise StopIteration()

        return self._elements[self.__pos]


class MemoryRepository:
    def __init__(self):
        self._data = {}

    def store(self, product: Product):
        if product.id in self._data:
            # Signal that we have a problem
            raise DuplicateIDError("Duplicate ID")
        self._data[product.id] = product

    def remove(self, product: Product):
        pass

    def find(self, product_id: int) -> Product:
        pass

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        """
        Methods returns an iterator over the repository

        What is a iterator?
            - a way to visit each element of a data structure, so that no elements are left out, and each element is
            visited only once
            - Iterator is a design pattern
            https://refactoring.guru/design-patterns/iterator
        """
        return RepositoryIterator(self._data.values())


class BinaryFileRepository(MemoryRepository):
    def __init__(self, file_name: str = "products.bin"):
        super().__init__()  # call to super constructor should be the first line in the method
        self._file_name = file_name
        self.__load_file()

    def store(self, product: Product):
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
