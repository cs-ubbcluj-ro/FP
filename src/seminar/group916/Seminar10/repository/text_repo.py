from seminar10.repository.memory_repo import MemoryRepository
from Seminar916.Seminar10.domain.car import Car
from Seminar916.Seminar10.domain.client import Client

class CarTextFileRepository(MemoryRepository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__loadFile()

    def __loadFile(self):
        lines = []
        try:
            fin = open(self.__fileName, "rt")
            # each car should be on its own line
            lines = fin.readlines()
            # close the file when done reading
            fin.close()
        except IOError:
            # It's ok if we don't find the input file
            pass

        for line in lines:
            current_line = line.split(",")
            newCar = Car(int(current_line[0].strip()), current_line[1].strip(), current_line[2].strip(), current_line[3].strip(), current_line[4].strip())
            # NOTE call super() so that we don't write the file we're reading from
            super().add(newCar)


    def __saveFile(self):
        fout = open(self.__fileName, "wt")

        for car in self:
            carString = str(car.id) + "," + str(car.licensePlate) + "," + str(car.getCarBrand()) + "," + str(car.getCarModel()) + "," + str(car.getCarColor()) + "\n"
            fout.write(carString)

        fout.close()

    def add(self, car: Car):
        super().add(car)
        self.__saveFile()


class ClientTextFileRepository(MemoryRepository):
    def __init__(self, filename):
        super().__init__()
        self.__fileName = filename
        self.__loadFile()

    def __loadFile(self):
        """
        Load the cars from a text file
        """
        # open a text file for reading
        # t - text file mode, r - reading
        lines = []

        try:
            fin = open(self.__fileName, "rt")
            # each car should be on its own line
            lines = fin.readlines()
            # close the file when done reading
            fin.close()
        except IOError:
            # It's ok if we don't find the input file
            pass

        for line in lines:
            current_line = line.split(",")
            newClient = Client(int(current_line[0].strip()), current_line[1].strip())
            # NOTE call super() so that we don't write the file we're reading from
            super().add(newClient)

    def __saveFile(self):
        """
        Save all cars to a text file
        """
        # open a text file for writing
        # t - text file mode, w - writing (rewrite the file every time)
        fout = open(self.__fileName, "wt")

        # writes car_string into the text file
        for client in self:
            client_string = str(client.id) + "," + str(client.name) + "\n"
            fout.write(client_string)

        # call close when done writing
        fout.close()

    def add(self, newClient: Client):
        # call the add() method on the super class
        # we want to do everything the superclass add() already does
        super().add(newClient)
        # we also want to save all cars to a text file
        self.__saveFile()


class RentalRepository(MemoryRepository):
    pass