from livecoding.calculator.functions.calculator import create_calculator, get_value_calculator, add_calculator, \
    undo_calculator
from livecoding.calculator.domain.rational import to_str
from livecoding.calculator.domain.rational_dict import create_rational, get_denominator, get_numerator


def print_menu():
    print("Calculator menu:")
    print("   + add a domain number")
    print("   u undo last operation")
    print("   x close the calculator")


def add_number_to_calculator_ui(calculator):
    num = int(input("numerator="))
    denom = int(input("denominator="))

    q = create_rational(num, denom)
    add_calculator(calculator, q)


def undo_calculator_ui(calc):
    undo_calculator(calc)


def run():
    calc = create_calculator()

    command_dict = {"+": add_number_to_calculator_ui, "u": undo_calculator_ui}

    while True:
        print("TOTAL: " + to_str(get_value_calculator(calc)))
        print_menu()

        option = input(">")

        if option in command_dict:
            try:
                command_dict[option](calc)
            except ValueError as ve:
                print(ve)
        elif option == "x":
            break
        else:
            print("Invalid command")

        # if option == "+":
        #     add_number_to_calculator(calc)
        # elif option == "x":
        #     break
        # else:
        #     print("Invalid command")


run()
