"""
What to do

1. Write a recursive function that determines the number of
even elements found on odd positions in a list of natural
numbers. Use a divide and conquer implementation that divides
the list into halves.
    V1 - The easiest one, using list slicing (data[0:m])

    V2 - Replace list slicing with the use of indices

    V3 - Replace the recursive implementation with an iterative
    one. (simulate the stack using a list or queue)

+ write a test function for the implementation

2. A stair can be climbed by going up 1, 2 or 3 steps at once.
Determine in how many ways we can go up a staircase of
10 stairs.
    1 stair = 1 way
    2 stairs = 2 ways (1+1, 2)
    3 stairs = 4 ways (1+1+1, 1+2, 2+1, 3)

    V1 - naive implementation
    V2 - dynamic programming

- Coin Change Problem
    V1 - Find the fewest number of coins needed to make a
    specific total

    V2 - Find the total number of ways to make a specific
    total

    say we have coins 1, 3 and 4
    the total sum is 8
    => take a look at the Excel file in the same folder as this source


Example problems
    Divide and Conquer
        - Calculate the r-th root of a given number x with a given precision p
        - Recursive Python 3 function using divide and conquer that returns the number of even numbers placed on odd positions
        in a list of natural numbers .
        Return None in case there is no such number
            V1 - using Python list slicing, divide the list into halves [time + extra space complexity]
            V2 - using indices, no list slicing [time + extra space complexity]
            V3 - eliminate recursion [time + extra space complexity]

    Dynamic Programming
        - A stair can be climbed by going up 1, 2 or 3 steps at once. Determine in how many ways we can go up a staircase
        of "n" stairs
        - Coin Change Problem
            V1 - Find the fewest number of coins needed to make a specific total (Greedy + DP)
            V2 - Find the total number of ways to make a specific total (naive + DP)
        - Given an array of integers, calculate the longest decreasing subsequence of primes contained in it

    Backtracking
        - A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and
    exactly once in each column. Generate all the N x N Latin squares for a given number N.
        - Variant: generate all the "reduced" Latin squares (these are squares where the letters in the first row and
        column are ordered).
"""


def v_2(arr: list, left, right) -> int:
    """
    time complexity:
        n = len(arr)
        T(n) = 2 * T(n/2) + 1

    extra-space complexity:
        T(n) = T(n/2) + 1
    """
    if not arr:
        return 0
    elif left == right:
        if arr[left] % 2 == 0 and left % 2 != 0:
            return 1
        else:
            return 0
    else:
        middle = (left + right) // 2
        first = v_2(arr, left, middle)
        second = v_2(arr, middle + 1, right)
        return first + second


def test_v_2():
    arr = [1, 2, 3, 4, 5, 6]  # - 3
    test_arr_1 = []  # - 0
    test_arr_2 = [1, 2, 3, 4, 5, 6, 7, 8]  # - 4
    test_arr_3 = [1]  # - 0
    test_arr_4 = [2, 2]  # - 1
    test_arr_5 = [2, 1, 2, 1, 2, 1, 2, 1]  # - 0

    assert v_2(arr, 0, len(arr) - 1) == 3
    assert v_2([], 0, len(test_arr_1) - 1) == 0
    assert v_2(test_arr_2, 0, len(test_arr_2) - 1) == 4
    assert v_2(test_arr_3, 0, len(test_arr_3) - 1) == 0
    assert v_2(test_arr_4, 0, len(test_arr_4) - 1) == 1
    assert v_2(test_arr_5, 0, len(test_arr_4) - 1) == 0


# test_v_2()

# Ciorbea Alina Alesia
def program_v3(list_nr, start, end):
    stack = [(start, end)]
    count = 0
    while stack:
        start, end = stack.pop()
        if start >= end:
            if start % 2 == 1 and list_nr[start] % 2 == 0:
                count += 1
        else:
            m = (start + end) // 2
            stack.append((m + 1, end))
            stack.append((start, m))
    return count


def test_case():
    assert program_v3([1, 1, 3, 1, 5], 0, 4) == 0
    assert program_v3([7, 8, 1, 2, 6], 0, 4) == 2
    assert program_v3([0, 0, 0, 1, 0, 1, 0], 0, 6) == 1
    assert program_v3([], 0, 0) == 0


# test_case()

# Coroiu ALexandra-Diana: v1 and the test
def count_even_on_odd_positions_v1(data):
    """
    Time complexity:
        T(n) = 2 * T(n/2) + 1
    Extra-space complexity:
        T(n) = T(n/2) + n
    """
    if not data:
        return 0
    if len(data) == 1:
        return 1 if data[0] % 2 == 0 else 0

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    return count_even_on_odd_positions_v1(left) + count_even_on_odd_positions_v1(right)


def test_count_even_on_odd_positions():
    data = [2, 3, 4, 7, 6, 9, 8]

    assert count_even_on_odd_positions_v1(data) == 4
    assert count_even_on_odd_positions_v1(data) == 4


# test_count_even_on_odd_positions()

# Moga Vlad-Mihai - Group 915
def count_ways_dynamic_programming(n):
    """
    Time complexity : O(n), where n is the number of stairs
    Extra-space complexity: O(n) for this implementation,
    can be reduced to O(1), as we only need the last 3
    values.
    """
    partial_sums = [0] * (n + 1)
    partial_sums[1] = 1
    partial_sums[2] = 2
    partial_sums[3] = 4

    for i in range(4, n + 1):
        partial_sums[i] = partial_sums[i - 1] + partial_sums[i - 2] + partial_sums[i - 3]

    return partial_sums[n]