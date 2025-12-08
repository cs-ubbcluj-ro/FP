What we already have
    1. IDObject and Car classes in the domain 
    2. CarRepository (in-memory) and TextFileCarRepository (text-files) repositoryies in the repo layer

What we want to add this time around:
    3. Add the Rental entity in the domain
        Rental class (inherits from IDObject):
            -> id         : int (inherited from IDObject)
            -> rented_car : Car (which car was rented)
            -> start      : date (builtin date type in Python), start of rental
            -> end        : date (builtin date type in Python), end of rental
    4. Add PyUnit tests for Car and Rental classes
        -> have at least 2 test functions in each test class
        -> run them with coverage information
           
    5. Add the RentalTextFileRepo class
        -> store Rental objects in a text file
        -> the car.id field identifies which car is referred by the rental

        When starting up the repositories:
            1. Initialize the car repository (this loads all cars from the file)
            2. Pass the car repository object to the constructor of the rental repository
            3. When reading car id's from the text file, you can find the car object using the CarRepository instance

    ex:
        cars.txt
        100, CJ 09 YHG, VW Polo, CarColors.WHITE

        rentals.txt
        200, 100, 2025-12-04, 2025-12-20

    for working with dates: look up the strptime() and strftime() functions
        
    BONUS POSSIBILITY:
    
    6. Write the CarService class
    7. Write the CompanyUI class
        -> allow adding a car from the console ui, so that it shows up in the text file :)





