"""
    1. Compute the factorial for a given positive integer
"""


def factorial(number: int) -> int:
    """
    Determine the factorial for the given non-negative integer
    input:
        number - input parameter
    output:
        number!
    """

    # This is  the base case, no recursion
    if number == 0:
        return 1

    # Recursive step progresses toward the simple case
    return number * factorial(number - 1)


def test_factorial():
    for n in range(0, 10):
        actual = factorial(n)

        expected = 1
        for i in range(1, n + 1):
            expected = expected * i

        assert actual == expected


'''
    2. Compute the sum of a list of numbers
'''


def sum_list(numbers: list) -> int:
    """
    Calculate the sum of the elements in the list
    input:
        lst - the list
    output:
        The sum of the elements
    """

    # This is  the base case, no recursion

    if len(numbers) == 0:
        return 0

    # Recursive step progresses toward the simple case
    return numbers[0] + sum_list(numbers[1:])


def test_sum_list():
    assert sum_list([]) == 0
    assert sum_list([0]) == 0
    assert sum_list([1, 2, 6]) == 9
    assert sum_list([-1, 4, -100, 50]) == -47
    assert sum_list([1, 2, 3, 4, 5, 6]) == 21


'''
    3. Compute the n-th term of the Fibonacci sequence
'''


def fibo(n: int) -> int:
    """
    Computes the n-th term of the Fibonacci sequence, where fib(0) = fib(1) = 1
    input:
        n - the index of the desired term
    output:
        The value of the desired term
    """

    # This is  the base case, no recursion
    if n == 0 or n == 1:
        return 1

    # Recursive step progresses toward the simple case
    return fibo(n - 2) + fibo(n - 1)


"""
    3a. Compute the n-th term of the Fibonacci sequence
    (tail call recursion - enabled, but not supported in Python, see:
        https://dev.to/rohit/demystifying-tail-call-optimization-5bf3
        https://tratt.net/laurie/blog/2004/tail_call_optimization.html
        http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html)
"""


def fib_tail_call(i: int, current_val: int = 1, next_val: int = 1) -> int:
    if i == 0:
        return current_val
    else:
        return fib_tail_call(i - 1, next_val, current_val + next_val)


def test_fibo():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for index in range(0, len(fib)):
        assert fibo(index) == fib[index]
        assert fib_tail_call(index) == fib[index]


'''
    4. Determine whether a given string is a palindrome
'''

"""
    4.1 This first version uses list slicing and uses more memory than required. Why?
"""


def palindrome(text: str) -> bool:
    """
    Determine if the given string is a palindrome; input string is case-sensitive and includes punctuation
    input:
        s - the string
    output:
        True if s is palindrome, False otherwise
    """

    # This is  the base case, no recursion
    if len(text) < 2:
        return True

    # Recursive step progresses toward the simple case
    # NB The text[1:-1] slice allocates memory for a new (smaller) list at each step
    return text[0] == text[-1] and palindrome(text[1:-1])


"""
    4.2 The second version does not use list slicing and avoid allocating additional memory in the call stack
"""


def palindrome_optimized(text: str) -> bool:
    """
    Check whether text reads identically forwards and backwards.

    Comparison is case-sensitive and includes spaces and punctuation.
    :param text: The string to check.
    :return: True if text is a palindrome, False otherwise.
    """
    return check_palindrome(text, 0, len(text) - 1)


def check_palindrome(text: str, left: int, right: int) -> bool:
    """Check the part of text between left and right, inclusively."""
    # Base case: no characters or just one character remain.
    if left >= right:
        return True

    # A mismatched pair means the string is not a palindrome.
    if text[left] != text[right]:
        return False

    # Move both indices inward without creating a new string.
    return check_palindrome(text, left + 1, right - 1)


def test_palindrome():
    assert palindrome("") is True
    assert palindrome("a") is True
    assert palindrome("axa") is True
    assert palindrome("axdf") is False
    assert palindrome("axdfdxa") is True
    assert palindrome("abcddcba") is True
    assert palindrome("abcddca") is False

    assert palindrome_optimized("") is True
    assert palindrome_optimized("a") is True
    assert palindrome_optimized("axa") is True
    assert palindrome_optimized("axdf") is False
    assert palindrome_optimized("axdfdxa") is True
    assert palindrome_optimized("abcddcba") is True
    assert palindrome_optimized("abcddca") is False


if __name__ == "__main__":
    test_factorial()
    test_sum_list()
    test_fibo()
    test_palindrome()
    print("All tests passed")
