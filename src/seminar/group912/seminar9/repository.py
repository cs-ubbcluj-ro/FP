from seminar.group912.seminar9.domain import Car, CarColors


class CarRepository:
    def __init__(self):
        # This is where we actually keep car data
        # Python dict() of car id (key) and car value (value)
        self._data = {}

    def store(self, object: Car):
        """
        Adds the car to the repository
        Raises DuplicateCarError in case a car with the given id
        is already stored
        """
        pass

    def find(self, car_id: int) -> Car:
        """
        Return the Car with the given id, if it exists. Otherwise,
        return None
        """
        pass

    def get_all(self) -> list[Car]:
        """
        Return a Python list of all the cars stored
        """
        pass


class TextFileCarRepository(CarRepository):
    def __init__(self, file_name: str = "cars.txt"):
        super().__init__()
        self._file_name = file_name
        self.__load_file()

    def __load_file(self):
        """
        Load the cars into memory. Reads the input text file and adds
        the cars to self._data
        """
        pass

    def store(self, object: Car):
        """
        Implement this method
        """
        pass

    def __save_file(self):
        """
        Save the cars in self._data to the text file

        This method should be called in the store() method, that
        this class needs to override :)

        Each Car should be on one line of the file
        1000, CJ 01 ERT, VW Polo, BLUE
        1001, VS 01 UIO, VW Passat, WHITE
        """
        pass


if __name__ == "__main__":
    # fout = open("example.txt", "wt")  # wt - write text file
    # fout.write("one string\n")
    # fout.write("another string\n")
    # fout.close()
    #
    # fin = open("example.txt", "rt")  # rt - read text file
    # lines = fin.readlines()
    # fin.close()
    #
    # for line in lines:
    #     # strip() removes the whitespace from the beginning and end
    #     # of the string
    #     print(line.strip())

    car_repo = TextFileCarRepository("my_cars.txt")
    car_repo.store(Car(1000, "AB 01 QWE", "VW Polo", CarColors.BLACK))
    car_repo.store(Car(1001, "SJ 02 RFV", "Audi A3", CarColors.BLACK))
    car_repo.store(Car(1002, "CT 03 TGB", "Dacia Jogger", CarColors.BLACK))
    # we should have 3 cars stored in the my_cars.txt file

    another_repo = TextFileCarRepository("my_cars.txt")
    # the cars are already read from the text file

    for c in another_repo.get_all():
        # display the 3 cars on the screen
        print(str(c.id) + " - " + c.licence + " - " + c.model)
