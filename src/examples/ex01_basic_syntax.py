# BASIC PYTHON SYNTAX
# Run this file on its own. Python executes these statements from top to bottom.
# Try predicting each result before running the corresponding section.
# Lines beginning with # are comments: they explain code but are not executed.


# 1. OUTPUT, VALUES AND NAMES
print("=== Values and names ===")

# print() displays values. Commas separate its arguments; by default, print()
# puts a space between them and moves to the next line after the last one.
print("Hello, Python!")
print("There are", 7, "days in a week.")

# = assigns a value to a name. No type declaration or semicolon is needed.
# Use descriptive names, with underscores between words (snake_case).
course_name = "Fundamentals of Programming"  # str: text
student_count = 150  # int: a whole number
lecture_hours = 2.0  # float: a floating-point number
is_first_year = True  # bool: True or False

print("Course:", course_name)
print("Student count:", student_count, type(student_count))
print("Lecture hours:", lecture_hours, type(lecture_hours))
print("First year:", is_first_year, type(is_first_year))
# type() reports the type of an object. Its output uses the word 'class'
# we will study classes later in the course.
# what you need to know now, is that a class is a data type


# 2. INPUT AND EXPLICIT CONVERSION
print("\n=== Input and conversion ===")  # \n starts a new line.
name = input("What is your name? ")
print("Nice to meet you,", name)
print("Type of the input:", type(name))

# input() ALWAYS returns a string, even when the user types digits.
# Enter a whole number such as 19. We assume valid input in this example.
# int() converts suitable text to an integer. Text such as 'hello' or '19.5'
# would cause a ValueError; handling errors is a later topic.
age_text = input("How old are you (in whole years)? ")
age = int(age_text)
print("As text, adding '1' gives:", age_text + "1")
print("As a number, adding 1 gives:", age + 1)
print("Before conversion:", type(age_text))
print("After conversion:", type(age))

# Python does not automatically convert between text and numbers for +.
# print("Your age is " + age)  # TypeError: str + int is not supported.
print("Your age is " + str(age))  # str() produces a string.
# Using print("Your age is", age) is another simple option.


# 3. ARITHMETIC AND COMPARISONS
print("\n=== Operators ===")
print("7 + 2 =", 7 + 2)
print("7 - 2 =", 7 - 2)
print("7 * 2 =", 7 * 2)
print("7 / 2 =", 7 / 2)  # / gives a float, even with integer operands.
print("7 // 2 =", 7 // 2)  # // rounds the quotient down (towards minus infinity).
print("7 % 2 =", 7 % 2)  # % gives the remainder: useful for divisibility.
print("7 ** 2 =", 7 ** 2)  # ** means exponentiation, not ^.
print("-7 // 2 =", -7 // 2)  # -4, not -3: especially worth noting from C/C++.

# Multiplication has higher precedence than addition. Use parentheses when
# you want a different order, or when they make an expression easier to read.
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# = assigns; == compares values. A comparison produces a bool.
print("Is 7 equal to 2?", 7 == 2)
print("Is 7 different from 2?", 7 != 2)
print("Is your age at least 18?", age >= 18)

# 4. STRINGS ARE SEQUENCES
# Sequences will appear again when discussing the list type and iterators
print("\n=== Strings ===")
language = "Python"
print("Length:", len(language))
print("First character:", language[0])  # Indexing starts at 0.

# NB! There exists a potential for nasty bugs if you don't consider the behaviour from the following line
print("Last character:", language[-1])  # -1 means the last item.

# You can slice into sequences; the example below starts at index 0 and ends at 1 (included)
print("First two characters:", language[0:2])  # Stop index 2 is excluded.

# Strings are immutable: their characters cannot be changed in place.
# language[0] = "J"  # TypeError. Keep this commented out during a normal run.

# 5. NAMES REFER TO OBJECTS
print("\n=== Assignment and identity ===")
original_word = "Python"
another_word = original_word  # Both names now refer to the same object.

# id() identifies an object, not a variable. It is unique among objects alive
# at the same time. Do not expect these exact ID numbers in another run, or
# rely on them being memory addresses in every Python implementation.
print("Original object ID:", id(original_word))
print("Same object ID:", id(another_word))

# This rebinds the name; does not modify the string
# Python 3 string are immutable, so they cannot be modified
another_word = another_word + " 3"
print("Original word:", original_word)
print("Reassigned word:", another_word)

# Objects have types; a name can later refer to an object of a different type.
value = 10
print("Before reassignment:", value, type(value))

# This is correct, but bad practice :(
# Reusing a name for an unrelated meaning usually hurts clarity, making the program harder to understand
value = "ten"
print("After reassignment:", value, type(value))
