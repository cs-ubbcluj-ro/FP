"""
    Determine the time complexity of the following algorithms as a function of n.
    sources:
        https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
        https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/
"""
from random import random

"""
    Time Complexity
    ---------------
    n - size of the program's input (this can the length of a list, array, it can be the 
    side of a matrix (n * n matrix), it can be an index (Fibonacci sequence))
    
    T(n) - function which approximates the number of operations the algorithm makes for
    input size "n"
    
    Once we have calculated/approximated T(n) we can state the complexity:
    
    O(n) - high bound, probably the most important, states that the algorithm cannot
    be more complex than this
    
    Omega(n) - low bound, the algorithm cannot have lower complexity than this
    
    Theta(n) - both low bound && high bound - this is best, becasue we have the 
    exact complexity

    Extra-space Complexity
    ---------------
    n - size of the program's input (this can the length of a list, array, it can be the 
    side of a matrix (n * n matrix), it can be an index (Fibonacci sequence))
    
    T(n) - function which approximates the additional memory space required by the algorithm 
    for input size "n" 
"""


def f_1(n: int):
    for i in range(10):  # number of iterations do not depend on n => constant time
        for j in range(n):  # depends on n, of course :)
            print("Hello World")  # constant time
    # T(n) = 10 * n * 1 => T(n) is a Theta(n) algorithm


"""
    What's the recipe?
        1. Determine on which input variable(s) does the algorithm complexity depend on
        2. Determine the value, or approximation for T(n) - when approximating, always go with higher values and O(n)
        3. Throw out the part of T(n) that is not at the maximum power and constant multiplicative factors    
        4. Determine complexity class (O(n) if approximating)
"""


def f_2(n: int):
    for i in range(n, n + 10):
        for j in range(n):
            print("Hello World")


def f_3(n: int):
    for i in range(1, n):
        for j in range(i, n):
            print("Hello World")
    # T(n) = (n - 1) + (n - 2) + ... + 2 + 1 = ((n-1) * n)/2  = n^2/2 - n/2 - 1/2 => T(n) is a Theta(n^2)


def f_4(n: int):
    for i in range(n):
        for j in range(2 * i + 1):
            print("Hello World")


def f_5(n: int):
    for i in range(n ** 2):  # n^2 iterations of the loop
        for j in range(i):  # j depends on i, which depends on n**2
            print("Hello World")


def f_6(n: int):
    for i in range(n):
        t = 1
        while t < n:
            print("Hello World")
            t *= 2  # we can multiply t by 2 a number of log_2(n) times before we no longer enter the loop


"""
    Time complexity depends on both "n" and "m"
"""


def f_7(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, m):
        print("Hello World")
    # T(n,m) = n + m


def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
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


def f_12(n: int) -> None:
    k = 0
    for i in range(n // 2, n):
        for j in range(2, n, pow(2, n)):
            k = k + n / 2


"""
    Analyze the time and space complexity 
"""


def f_13(data: list) -> int:
    data_sum = 0
    for el in data:
        j = len(data)
        while j > 1:
            data_sum += el * j
            j = j // 3
    return data_sum


def f_14(data: list) -> int:
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_14(data[:m]) + f_14(data[m:])


"""
    Time Complexity (we assume list slicing is constant time)
    ---------------
    n - is the length of the input list
    
    T(n) = 1, n <= 1
         = 2 * T(n/2) + 1
         
    T(n) = 2 * [ 2 * T(n/4) + 1 ] + 1 = 4 * T(n/4) + 2 + 1
    T(n) = 4 * [ 2 * T(n/8) + 1 ] + 2 + 1 = 8 * T(n/8) + 4 + 2 + 1
    T(n) = 16 * T(n/16) + 8 + 4 + 2 + 1
    
    -- at one point, T(n/something) = T(1), so a number k must exist so that 2^k = n
    
    T(n) = 2^k * 1 + 2^(k-1) + ... + 2 + 1 = 2^(k+1) - 1 = 2n - 1

    Extra-space Complexity
    ---------------
    n - is the length of the input list
    
    T(n) = 1, n <= 1
         = 2 * T(n/2) + n/2 + n/2
    (we solve the same way as in case of the time complexity)
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
    Time Complexity
    ---------------
    T(n) = 1, n <= 1
         = 4 * T(n/2) + 1, n > 1
    (solve the same way as before)
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


def f_17_better(data: list) -> int:
    aux = sorted(data)  # usually n * log_2(n)
    max_count = 1
    current_count = 1
    for i in range(0, len(aux) - 1):  # n
        if aux[i] == aux[i + 1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1
    return max_count


data = [1, 1, 1, 1, 1, 1]
print(f_17(data))
print(f_17_better(data))

"""
    What is the time complexity when implementing the following algorithm. How can this be 
    optimized and how will that improve the complexity?
"""


def f_18(x, n: int):
    """
    The algorithm returns x ** n, n is positive integer
    :param x:
    :param n:
    :return:
    """
    # TODO Implement me
    pass
