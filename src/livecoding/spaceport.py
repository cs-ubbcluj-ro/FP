"""
Basic git operations
    1. clone -> download the git repository locally (on my laptop)
    2. add -> tells git to add the file to the repository
    3. commit -> integrates the changes into the local copy of the git repository
    4. push -> synchronizes all the local commits to the server copy of the git repository
    5. pull -> download the changes that other people have pushed to the server git repository
"""

"""
Spaceport Control: Clear for Landing?

Landing codes are assumed to contain only decimal digits, with no sign.
"""


# Stage 2: calculate the checksum and decide the landing status.
def sum_digits(code: int) -> int:
    """
    Return the sum of the decimal digits of code.

    :param code: A non-negative integer.
    :return: The digit sum as an integer; return 0 for code 0.
    """
    total = 0

    # For code 0, the loop is skipped and the total remains 0.
    while code > 0:
        digit = code % 10
        total = total + digit
        code = code // 10

    return total


def landing_status(checksum: int) -> str:
    """
    Return the landing status determined by checksum modulo 3.

    :param checksum: A non-negative integer.
    :return: "CLEARED" for remainder 0,
             "MANUAL CHECK" for remainder 1,
          or "HOLD" for remainder 2.
    """
    remainder = checksum % 3

    if remainder == 0:
        return "CLEARED"
    elif remainder == 1:
        return "MANUAL CHECK"
    else:
        return "HOLD"


# Stage 3: group the inspection results in a dictionary.
def build_report(code: int) -> dict:
    """
    Create an inspection report without reading or printing anything.

    :param code: A non-negative integer.
    :return: A new dictionary with the keys "code", "checksum", and "status".
    """
    checksum = sum_digits(code)
    status = landing_status(checksum)

    report = {"code": code, "checksum": checksum, "status": status}
    return report


def print_report(report):
    """
    Display an inspection report and its landing message.

    :param report: A dictionary in the format returned by build_report.
    :return: None. The report is displayed and is not modified.
    """
    print("Landing code:", report["code"])
    print("Checksum:", report["checksum"])
    print("Status:", report["status"])

    if report["status"] == "CLEARED":
        print("Welcome! You may land.")
    elif report["status"] == "MANUAL CHECK":
        print("Please wait while we find someone responsible.")
    else:
        print("Stay in orbit. The coffee machine is blocking the runway.")


def main():
    """
    Run the console menu and keep the flight log for this session.

    Landing-code input must contain one or more decimal digits (0-9).
    :return: None. The function ends when the operator chooses "0".
    """
    # Stage 1: greet the operator. input() returns a string.
    operator_name = input("Operator name: ")

    # We use f-strings to make it easier to insert variable values into the string
    print(f"Welcome to Spaceport Control {operator_name}!")

    # Stage 5: this local list stores reports in inspection order.
    flight_log = []

    # Stage 4: keep showing the menu until the operator chooses to exit.
    while True:
        print()
        print("1. Inspect a landing code")
        print("2. Show the flight log")
        print("0. Close the control tower")
        choice = input("Choose an option: ")

        if choice == "1":
            code_text = input("Landing code (non-negative integer): ")
            code = int(code_text)

            report = build_report(code)
            print_report(report)
            flight_log.append(report)

        elif choice == "2":
            print("Flight log")

            if len(flight_log) == 0:
                print("No spaceships inspected yet.")
            else:
                for report in flight_log:
                    print()
                    print_report(report)

            print("Total inspections:", len(flight_log))

        elif choice == "0":
            print("Control tower closed. Goodbye, " + operator_name + "!")
            break

        else:
            print("Aliens!?")


# Start the console application when this file is run directly.
if __name__ == "__main__":
    main()
