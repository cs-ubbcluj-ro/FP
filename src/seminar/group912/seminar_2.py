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
    Below this line we write functions that implement functionalities
        - We do not read/write from/to the console
        - We never use global variables/module variables
        - We use input parameters and return values
"""


def create_city(city_name: str, city_pop: int, city_county: str) -> dict:
    # city represented as a Python dict
    # "city" -> key, city_name -> value (actual city name as str)
    return {"city": city_name, "population": city_pop, "county": city_county}


def get_city_name(city: dict) -> str:
    return city["city"]


def get_city_pop(city: dict) -> str:
    return city["population"]


def get_city_county(city: dict) -> str:
    return city["county"]


"""
    Below this line we write the user interface
        - All print/input statements go below this line
        - In this part we should not have a lot of processing
        (user input/output is hard to test automatically)
"""


def print_menu() -> None:
    print("1. Sort the cities")
    print("2. Display the list of cities")
    print("3. Search for a city (using partial, case-insensitve str matching)")
    print("4. Add a city from the console")
    print("5. Add a number of random cities to the list (the number is read from the console)")
    print("6. Quit")


def start():
    """
    This acts like the main() function of a C program :)
    """
    while True:
        print_menu()

        option = int(input("Enter your choice: "))
        if option == 1:
            continue
        elif option == 6:
            # exit the nearest running loop (the while in this case)
            break
        else:
            # runs in case none of the above
            print("Invalid input")


# represent the city using a list
# What is a list?
#   - each element has a predecessor and a successor
#   - elements can be accessed by their index (list is sorted)
# vatra_dornei = ["Vatra Dornei", 10000, "Suceava"]
# print("Ciy name: " + vatra_dornei[0])

# represent the city using a dict
# What is a dict?
#   - pairs of key/value elements where keys are unique and (in Python) immutable (numbers, str, tuples)
#   - there is no ordering, so no accessing elements using their index
# suceava_as_list = ["Suceava", 100000, "Suceava"]
# suceava_as_dict = {"city_name": "Suceava", "city_population": 100000, "city_county": "Suceava"}
# print("Ciy name: " + suceava_as_dict["city_name"])

# x = create_city("Vatra Dornei", 10000, "Suceava")
# print(type(x))


# print("City name: " + x["city"] + ", population: " + str(x["population"]) + ", county: " + x["county"])
# print("City name: " + get_city_name(x) + ", population: " + str(get_city_pop(x)) + ", county: " + get_city_county(x))

start()
