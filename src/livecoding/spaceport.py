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


operator_name = input("What is your name?")

# Using string concatenation
print("Welcome to the control tower " + operator_name)

# Using Python f-strings
print(f"Welcome again to the control tower {operator_name}")

# for those of you using macOS
# in Trminal: git --version
# Will prompt to install Xcode command line tools that include git

landing_code = input("Landing code: ")
landing_code_int = int(landing_code)
checksum = calculate_checksum(landing_code_int)
print(checksum)
