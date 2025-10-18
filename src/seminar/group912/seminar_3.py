"""
    Determine the time complexity of the following algorithms as a function of n.
    sources:
        https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
        https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/
"""
from random import random

"""
    n -> size of the program's input (ex. length of array to sort, the n-th term of Fibonacci, n^2 might be the size of
         a matrix
         
    T(n) -> how many operations the algorithm does for input size "n".
            ex.
                if T(n) = 1 => constant time (usually,  very fast algorithm)
                   T(n) = 2^n => exponential time (usually, very slow algorithm :( )
                   
            time (or memory complexity)
            O(n)        - high bound (the function cannot be slower than this)
            Omega(n)    - low bound (usually not that useful)
            Theta(n)    - this is the best, it means we have both low-bound and a high-bound
"""


def f_1(n: int):  # the n input parameter is used for time complexity
    for i in range(10):  # does not depend on size of n => constant time ( time = 1 )
        for j in range(n):  # depends on n ( n iterations )
            print("Hello World")  # constant time

    # 1. Determine the value of T(n)
    # T(n) = 10 * n * 1 = 10 * n
    # 2. Disregard all terms of "n" that are not at the highest power (we don't have any)
    # 3. Throw out constant multiplicative factors (goodbye 10)
    # 4. We're left with T(n) = n => T(n) belongs to Theta(n)


def f_2(n: int):
    for i in range(n, n + 10):  # does not actually depend on the size of n
        for j in range(n):  # like before
            print("Hello World")  # constant time
    # T(n) = n


def f_3(n: int):
    for i in range(1, n):
        for j in range(i, n):  # (n-1) + (n-2) + ... + 1 -- this accounts for the for loop above
            print("Hello World")
    # T(n) = (n-1)(n-2)/2 => Theta(n^2)


def f_4(n: int):
    for i in range(n):
        for j in range(2 * i + 1):
            print("Hello World")
    # T(n) = n * ( n - 1 ) + n
    # T(n) = 1 + 3 + 5 + ... + 2n - 1 => T(n) = n^2


def f_5(n: int):
    for i in range(n ** 2):  # n^2
        for j in range(i):  # n^2 - 2
            print("Hello World")
    # T(n) = 1 + 4 + 9 + 16 + ... + n^2 => O(n^4)
    # n = 10 => 1 second
    # n = 20 => 16 seconds


def f_6(n: int):
    for i in range(n):
        t = 1
        while t < n:
            print("Hello World")
            t *= 2
    # T(n) = log_2(3) + log_2(4) + ... + log_2(n-1)
    # we can approximate with log_2(n), which is greater than the actual value
    # T(n) = n * log_2(n) => O(n * log_2(n))


"""
    Time complexity depends on both "n" and "m"
"""


# T(n, m) = n + m
def f_7(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, m):
        print("Hello World")


def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


def f_9(n: int):  # T(n) = n^2 => Theta(n^2)
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):  # non-nested loops do not increase complexity, they increase the constant
            # multiplicative factor
            print("Hello World")


def f_10(n: int):
    for i in range(n):
        for j in range(n, i, -1):
            print("Hello World")


def f_11(n: int, m: int) -> None:
    a = 0
    b = 0
    for i in range(n):
        a = a + random()

    for i in range(m):
        b = b + random()


count = 0


def f_12(n: int) -> None:
    global count
    k = 0
    for i in range(n // 2, n):
        for j in range(2, n, pow(2, n)):  # range(2, n, 2**n)
            k = k + n / 2
            count += 1


# for i in range(1, 10_000,100):
#     count = 0
#     f_12(i)
#     print(i, count)

"""
    Analyze the time and space complexity 
"""


def f_13(data: list) -> int:
    data_sum = 0
    for el in data:  # n iterations, where n is the length of list data
        j = len(data)  # j = n
        while j > 1:  # log_3(n) times
            data_sum += el * j
            j = j // 3
    return data_sum


# Time: T(n) = n * log_3(n),
# When considering extra space complexity, we disregard the size of the input data
# Space: T(n) = Theta(1)


def f_14(data: list) -> int:
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_14(data[:m]) + f_14(data[m:])


"""
Time complexity:
    n - length of the input list "data"

    T(n) = 1, n <= 1
         = 2 * T(n/2) + 1, n > 1 (we ignore time required to create array copy)
    
    T(n) = 2 * T(n/2) + 1 = 2 * [ 2 * T(n/4) + 1 ] + 1 = 4 * T(n/4) + 2 + 1
    T(n) = 4 * [ 2 * T(n/8) + 1 ] + 2 + 1 = 8 * T(n/8) + 4 + 2 + 1
    
    T(n) = 16 * T(n/16) + 8 + 4 + 2 + 1
    we reach the point where n/something = 1 => we consider k, so that 2^k = n
    
    T(n) = 2^k * T(1) + 2^(k-1) + ... + 2^0 
    T(n) = 2^k * 1 + 2^k - 1 = 2 * n => Theta(n)
    
Space complexity:
    n - length of the input list "data"
    
    T(n) = 1, n <= 1 
         = 2 * T(n/2) + n/2 + n/2
    (have to do the same calculation as above)
"""


def f_15(n: int) -> int:
    s = 0
    for i in range(1, n ** 2):
        j = i
        while j != 0:
            s = s + j - 10 * j // 10
            j //= 10
    return s


def f_16(n, i: int) -> None:
    if n > 1:
        i *= 2
        m = n // 2
        f_16(m, i - 2)
        f_16(m, i - 1)
        f_16(m, i + 2)
        f_16(m, i + 1)
    else:
        print(i)


"""
    Time complexity:
    
    T(n) = 1, n <= 1
         = 4 * T(n/2) + 1
    (solve the same way as f_14)
    
"""

"""
Analyze the algorithm's time complexity. Write an equivalent algorithm with 
a strictly better time complexity
"""


def f_17(data: list) -> int:
    i = 0
    j = 0
    m = 0
    c = 0
    while i < len(data):
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data):
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m


"""
    The number of appearances of the most frequent number in the list, complexity is O(n^2)
"""


def f_17_better(data: list) -> int:
    frequencies = {}
    max_f = 0
    for n in data:  # n iterations
        if n not in frequencies:  # either constant time or log_2
            frequencies[n] = 1
        else:
            frequencies[n] += 1
        max_f = max(max_f, frequencies[n])
    return max_f


"""
    What is the time complexity when implementing the following algorithm. How can this be 
    optimized and how will that improve the complexity?
"""


def f_18(x, n: int):
    """
    The algorithm returns x ** n, assume n a positive integer
    :param x:
    :param n:
    :return:
    """
    # TODO Implement me
    pass
