from calc import create_calculator, add_to_calculator, get_calculator_value
# from rational_as_list import create_rational, to_str
from rational_as_dict import create_rational, to_str


# -----------------------#
# Only UI functions here #
# -----------------------#


def print_menu():
    print("Calculator menu:")
    print("   + add a rational number")
    print("   u undo last operation")
    print("   x close the calculator")


def add_number_ui(calculator):
    # TODO Make sure we add additional checks here
    value = input("Enter number (a/b format):")
    tokens = value.split("/")
    # FIXME denominator is 0 --- halp!
    q = create_rational(int(tokens[0]), int(tokens[1]))
    add_to_calculator(calculator, q)


def undo_ui(calculator):
    pass


def start():
    calculator = create_calculator()
    commands = {"+": add_number_ui, "u": undo_ui}

    while True:
        print_menu()
        print("TOTAL: " + to_str(get_calculator_value(calculator)))
        option = input(">").strip()
        if option in commands:
            try:
                commands[option](calculator)
            except ValueError as a:
                print(a)
        elif option == "x":
            print("Bye!")
            return
        else:
            print("Invalid input")


if __name__ == "__main__":
    start()
