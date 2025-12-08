from seminar.group912.seminar10.domain.car import Car, CarColors


class DuplicateCarError(Exception):
    pass


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
        if object.id in self._data:
            raise DuplicateCarError("Car with the given id already exists")
        self._data[object.id] = object

    def find(self, car_id: int) -> Car:
        """
        Return the Car with the given id, if it exists. Otherwise,
        return None
        """
        if car_id in self._data:
            return self._data[car_id]
        return None

    def get_all(self) -> list[Car]:
        """
        Return a Python list of all the cars stored
        """
        return list(self._data.values())


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
        try:
            with open(self._file_name, "rt") as fin:
                for line in fin:
                    line = line.strip()
                    if not line:
                        continue

                    car_id_str, license_plate, model, color_str = [p.strip() for p in line.split(",")]
                    car = Car(int(car_id_str), license_plate, model, CarColors[color_str])

                    self._data[car.id] = car
        except FileNotFoundError:
            pass

    def store(self, object: Car):
        """
        Implement this method
        """
        super().store(object)
        self.__save_file()

    def __save_file(self):
        """
        Save the cars in self._data to the text file

        This method should be called in the store() method, that
        this class needs to override :)

        Each Car should be on one line of the file
        1000, CJ 01 ERT, VW Polo, BLUE
        1001, VS 01 UIO, VW Passat, WHITE
        """

        fout = open(self._file_name, "wt")

        for car in self._data.values():
            fout.write(f"{car.id}, {car.license_plate}, {car.model}, {car.color.name}\n")

        fout.close()


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
    # car_repo.store(Car(1000, "AB 01 QWE", "VW Polo", CarColors.BLACK))
    # car_repo.store(Car(1001, "SJ 02 RFV", "Audi A3", CarColors.RED))
    # car_repo.store(Car(1002, "CT 03 TGB", "Dacia Jogger", CarColors.BLUE))
    # car_repo.store(Car(1003, "GH 05 UJM", "Honda Civic", CarColors.YELLOW))
    # car_repo.store(Car(1005, "KL 06 BGT", "BMW X5", CarColors.MAGENTA))

    # another_repo = TextFileCarRepository("my_cars.txt")
    # the cars are already read from the text file

    for c in car_repo.get_all():
        # display the 3 cars on the screen
        print(str(c.id) + " - " + c.license_plate + " - " + c.model)
