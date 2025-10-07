"""
What we want to do today
    1. Build a simple menu on the console
    2. Work with Python's list and dict types
    3. Generate some random entities in the program (because we don't like to type too much)
    4. How to structure this small program :)

Problem statement:
    -- We want to manage a list of cities. Each city has a name, population, county
What the program needs to do (requirements):
    1. Sort the cities
    2. Display the list of cities
    3. Search for a city (using partial, case-insensitve str matching)
    4. Add a city from the console
    5. Add a number of random cities to the list (the number is read from the console)
    6. Quit
"""

"""
    Below this comment we add functions that implement the required functionalities
        - There is not user input/output here (no print, no input)
        - We have function parameters and return values
        - No global variables/module variables
"""

"""
    Function naming 101 :)
        1. Most function names should have a verb - what do they do
        2. Functions that return entity attributes (e.g, get_city_name) should start with get_ (in object oriented
        code, these are getters)
        3. Opposite of 2. are setters (functions that set entity attributes) (e.g., set_city_name() )
"""

"""
Here each city is represented as a list

def create_city(city_name: str, city_pop: int, city_county: str) -> list:
    return [city_name, city_pop, city_county]


def get_city_name(city: list) -> str:
    return city[0]


def get_city_pop(city: list) -> int:
    return city[1]


def get_city_county(city: list) -> str:
    return city[2]
"""


# Here each city is represented as a dict
def create_city(city_name: str, city_pop: int, city_county: str) -> dict:
    return {"city": city_name, "population": city_pop, "county": city_county}


def get_city_name(city: dict) -> str:
    return city["city"]


def get_city_pop(city: dict) -> int:
    return city["population"]


def get_city_county(city: dict) -> str:
    return city["county"]


def to_str(city: dict) -> str:
    return "City of " + get_city_name(city) + ", population=" + str(get_city_pop(city)) + " is in " + get_city_county(
        city)


"""
    Below this comment we add the user interface
        - All print/input statements go here
        - In the future we try to write test functions for the program, which means that this part shoud not do
        too much
"""


def add_city(city_list: list) -> bool:
    city_name = input("Enter city name: ")

    for city in city_list:
        if city_name == get_city_name(city):
            return False

    # Error in case the value cannot be converted to a base 10 int
    city_pop = int(input("Enter city population: "))
    city_county = input("Enter city county: ")

    new_city = create_city(city_name, city_pop, city_county)
    city_list.append(new_city)
    return True


def display_cities(cities_list) -> None:
    print("\nList of all cities:")
    for city in cities_list:
        print(to_str(city))
    print("")


def print_main_menu() -> None:
    """
    It's ok to write a function just in order to group some code
    """
    print("1. Sort the cities")
    print("2. Display the list of cities")
    print("3. Search for a city (using partial, case-insensitve str matching)")
    print("4. Add a city from the console")
    print("5. Add a number of random cities to the list (the number is read from the console)")
    print("6. Quit")


def start():
    """
    The program's entry point. Similar to a C program's main function
    """

    # We keep the list of cities here, and pass it as an input parameter to all functions that require it
    cities_list = [create_city("Pitesti", 112_000, "Arges"), create_city("Braila", 100_000, "Braila"),
                   create_city("Zalau", 53_000, "Salaj")]

    while True:
        print_main_menu()
        option = int(input("Enter your choice: "))
        if option == 2:
            # It's ok to add a function in order to keep the program's main loop clean
            display_cities(cities_list)
        elif option == 4:

            # print("Local values:")
            # print(locals())

            # print("Global values:")
            # print(globals())

            if add_city(cities_list) is True:
                print("City added successfully")
            else:
                print("Failed to add city")

        elif option == 6:
            print("Bye bye")
            break
        else:
            print("Invalid menu option")


# We group all city attributes into the same list
# targu_neamt = ["Targu Neamt", 20_000, "Neamt"]

# Print out the city pop, it's easy to lose track of what [1] means !?
# print(targu_neamt[1])  # [1] means population
# commenting out has a few issues too
#   - we can't change what [1] does without recommenting everything
#   - at one point, people forget :(

# my_city = create_city("Alba Iulia", 60_000, "Alba")
# print(type(my_city))

# print("The city of " + get_city_name(my_city) + " with a population of " + str(get_city_pop(
#     my_city)) + " in the county of " + get_city_county(my_city) + ".")

# print(to_str(my_city))

start()
