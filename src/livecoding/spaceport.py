"""
Basic git operations
    1. clone -> download the git repository locally (on my laptop)
    2. add -> tells git to add the file to the repository
    3. commit -> integrates the changes into the local copy of the git repository
    4. push -> synchronizes all the local commits to the server copy of the git repository
    5. pull -> download the changes that other people have pushed to the server git repository
"""


# print("Hello world!")

# print, input are builtin Python 3 functions
# input returns an str

def calculate_checksum(flight_code: int) -> int:
    """
    Calculates flight code checksum
    :param flight_code: The flight code
    :return: The digit checksum
    """
    code = 0

    while flight_code > 0:
        last_digit = flight_code % 10
        code += last_digit
        # / is real number division (result is a float), // is integer division (result is an int)
        flight_code = flight_code // 10
    return code


def get_flight_status(checksum: int) -> str:
    if checksum % 3 == 0:
        return "CLEARED"
    elif checksum % 3 == 1:
        return "MANUAL CHECK"
    else:
        # None of the conditions above
        return "HOLD"


def create_report(flight_code: int, checksum: int, status: str) -> dict:
    # Python's dict is a collection of key, value pairs, where keys are unique
    return {"CODE": flight_code, "CHECKSUM": checksum, "STATUS": status}


operator_name = input("What is your name?")
# Using string concatenation
print("Welcome to the control tower " + operator_name)

# Using Python f-strings
# print(f"Welcome again to the control tower {operator_name}")

# for those of you using macOS
# in Trminal: git --version
# Will prompt to install Xcode command line tools that include git

# Empty Python list
flight_reports_list = []

while True:
    print()
    print("1. Read landing code information")
    print("2. Exit")

    option = input(">")
    if option == "1":
        landing_code = input("Landing code: ")
        landing_code_int = int(landing_code)
        checksum = calculate_checksum(landing_code_int)
        status = get_flight_status(checksum)

        flight_report = create_report(landing_code_int, checksum, status)
        print(flight_report)
        flight_reports_list.append(flight_report)
        # print(f"Flight with code {landing_code} has checksum {checksum} and status {status}")
    elif option == "2":
        break
    else:
        # None of the valid options
        print("Invalid option. Aliens !!??")
