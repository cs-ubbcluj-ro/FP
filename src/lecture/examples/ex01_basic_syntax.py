# Introduction to basic Python built-in functions and types

# print(): Used to display output
print("Hello! This program will introduce you to some Python basics.")

# input(): Used to get user input from the console as a string
name = input("What is your name? ")
print("Nice to meet you,", name)
# Let's check that name indeed has the Python type str.
print(type(name))

# int(): Attempt to convert a string into an integer - the integer base can be provided as an optional, additional
# parameter; the default base is 10
age_str = input("How old are you? ")
age = int(age_str)  # converts string to an integer
print("In one year, you will be", age + 1)

# type(): Shows the data type of a value or variable
# Notice the type says 'class', as basically everything in Python 3 is implemented as a class
# We will cover classes and objects during the second part of the course
print("The type of your name is:", type(name))
print("The type of your age is:", type(age))

# id(): Returns a unique identifier for an object in memory
print("The memory ID of your name variable is:", id(name))
print("The memory ID of your age variable is:", id(age))
