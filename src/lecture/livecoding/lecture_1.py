"""
Problem statement:
    1. Read a string from the program's console
    2. Divide the string into numbers, words (using space)
    3. Build a list of primes, a list of negative numbers, a list of the rest of the numbers, a list
    of capitalized names

    4. Print out all primes numbers etc. in ascending order, without duplicates :)
"""
print("Hello World")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


user_input = "55 -6 67 90 9 56 -2 56 -6 -6" #input("Enter a string: ")
# built-in type() function
# print(type(user_input))
tokens = user_input.split()
print(tokens)

prime_numbers = []
negative_numbers = []
other_numbers = []

for token in tokens:
    try:
        int_token = int(token)
    except ValueError:
        continue
    if is_prime(int_token):
        prime_numbers.append(int_token)
    elif int_token < 0:
        negative_numbers.append(int_token)
    else:
        other_numbers.append(int_token)

negative_numbers = sorted(list(set(negative_numbers)))

print("primes ",prime_numbers)
print("negative ",negative_numbers)
print("other ",other_numbers)