"""

Create a calculator program for rational numbers with the following
functionalities:
    + add a rational number to the calculator
    u undo the last operation
    x exit
"""
from math import gcd


# ----------------------#
# Non-UI functions here #
# ----------------------#

# Functions to handle rational numbers


# Calculator functions
# The calculator stores:
#   (1) current value : rational number (initially 0, when starting the program)
#   (2) history of previous values: list<rational numbers>


# -----------------------#
# Only UI functions here #
# -----------------------#


def print_menu():
    print("Calculator menu:")
    print("   + add a rational number")
    print("   u undo last operation")
    print("   x close the calculator")
