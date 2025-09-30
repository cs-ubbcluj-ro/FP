"""
Basic git operations to get you started
    -> clone - bring a remote repository to my local computer (retain all git information)
    -> commit - notify git which changes you want it to remember and store
    -> push - push my changes back to the remote repository

NB!
    -> git - a source control version system
    -> github.com - a web platform for managing git repositories

"""

"""
1. Given 2 integers a and b, return True if one of them is 10 or if their sum is 10
"""


# a and b should be ints (int is the Python type for integer) but this is only a type hint
def function_for_value_10(a: int, b: int) -> None:
    if a == 10 or b == 10 or a + b == 10:
        print("true")
    else:
        print("false")


# function_for_value_10(1, 9)
# function_for_value_10("4", "6")

"""
2. Write a Python program which iterates the integers from 1 to 50. 
    - For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    - For numbers which are multiples of both three and five print "FizzBuzz".
"""


def fizz_buzz():
    for i in range(1, 51):  # the left bound is included, the right bound is not
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz")
        elif i % 5 == 0:  # if / elif / elif / ... / else replaces the switch statements
            print(i, "Buzz")
        elif i % 3 == 0:
            print(i, "Fizz")  # print function has variable number of arguments


"""
3. Write a program that reads temperatures in Celsius from the user (until they enter q), stores them in a list, 
    and then prints:
    - all entered temperatures,
    - the average, minimum, maximum and median temperature,
    - a new list with the values converted to Fahrenheit.
"""

"""
    input() - read from console
    int() - try to convert its parameter to a Python integer
            -> Error in case it cannot be done
"""


def temperatures() -> None:
    # temps_list = list()  # list() is the constructor for type list
    temps_list = []  # start with an empty list

    while True:
        temp = input("Enter temperature in Celsius:")
        if temp == "q":
            break  # stops the execution of the innermost loop
        temps_list.append(int(temp))

    print("All temperatures: ", temps_list)

    # / -> real number division
    # // -> int division
    if len(temps_list) > 0:
        print("The average: ", sum(temps_list) / len(temps_list))
        print("Minimum: ", min(temps_list))
        print("Maximum: ", max(temps_list))

        temps_list.sort()
        print("Median: ", temps_list[len(temps_list) // 2])
    else:
        print("Cannot calculate stats")

    # print(type(temp))  # type() is a Python built-in function that returns the type of the variable
    # print(temp)


"""
4. Given a non-empty string like "Code" return a string like "CCoCodCode"
    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
"""


def string_splosion(s: str) -> str:
    splosion = ""
    for index in range(1, len(s) + 1):
        splosion += s[:index] # splosion = splosion + s[:index]
    return splosion


print(string_splosion("Code"))

"""
5. Word Frequency Counter
    - Given a sentence entered by the user, split it into words and count how many times each word occurs.
"""

"""
6. Write a function that checks if two words are anagrams of each other by comparing letter frequencies using a dictionary.
"""

"""
7. Read pairs of student names and grades until the user enters "done". Store them in a dictionary with the student name 
    as key and a list of grades as value. Then compute:
    - average grade per student,
    - overall average,
    - the top student(s). To be in contention for "top student", students must have at least 3 grades
"""
