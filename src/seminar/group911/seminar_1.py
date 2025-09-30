print("Hello group 911!")
"""
Basics of working with git:
    1. clone -> create a local (on your laptop) copy of the remote repository; this local copy is linked with its 
    remote version
    2. commit -> you record the changes on your laptop to the local copy of the git repository; (at this point, the
    changes do not show up on the remote repository
    3. push -> update the remote repository with the changes you made locally
"""

"""
1. Given 2 integers a and b, return True if one of them is 10 or if their sum is 10
"""
a = 5  # first, a receives the type from the right hand side expression, then it receives its value
b = 6


# print(str(a) + str(b))  # str() convert to string (str is the Python data type for string)
#
# a = "5"
# b = "911"
#
# print(type(a))
# print(type(b))
#
# print(int(a) + int(b))


def function_10(a: int, b: int) -> bool:
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


print(function_10(a, b))
print(function_10("1", "0"))
"""
2. Write a Python program which iterates the integers from 1 to 50. 
    - For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    - For numbers which are multiples of both three and five print "FizzBuzz".
"""

"""
3. Write a program that reads temperatures in Celsius from the user (until they enter q), stores them in a list, and then prints:
    - all entered temperatures,
    - the average, minimum, maximum and median temperature,
    - a new list with the values converted to Fahrenheit.
"""

"""
4. Given a non-empty string like "Code" return a string like "CCoCodCode"
    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
"""

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
