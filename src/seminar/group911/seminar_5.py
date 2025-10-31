"""
    Dynamic programming
    1. Overlapping subproblems - how do we define them (mathematically, formula)
    2. Memoization - avoid recalculating results again and again by storing them
        in a data structure and recalling them in O(1) time when needed.
    3. Principle of optimality - solutions to the subproblems are solutions in themselves

    What is dynamic programming?
    => a way to optimize solving a class of problems by avoiding repeated calculations
"""
from xml.etree.ElementInclude import include

"""
    1. Calculating the n-th term of the Fibonacci sequence
"""

"""
    2. Calculate the maximum subarray sum 
    (subarray = elements having continuous indices)
"""
array = [2, -3, -1, 3, 4, -3, -1, 1, 1, 3, -4, 2, 3, -1, 5]
# array = [-2, -3, -1, -3, -4, -3, -1, -1, -1, -3, -4, -2, -3, -1, -5]
# print(sum(array[3:]))
"""
    Possible solutions:
        1. naive implementation = 2 for loops => O(n^2) complexity
        2. divide & conquer = 2 recursive calls + O(n)
            T(n) = 2 * T(n/2) + n => O(n * log(n)) also Theta(n * log(n)) complexity
        3. dynamic programming (below)
"""


def max_subarray_sum(array: list) -> int:
    current_sum = array[0]  # best sum ending at the current index
    global_sum = array[0]  # best sum we've seen so far

    for i in range(1, len(array)):
        # if current_sum + array[i] < array[i]:
        if current_sum < 0:
            current_sum = array[i]
        else:
            current_sum += array[i]
        global_sum = max(global_sum, current_sum)

    return global_sum


# print(max_subarray_sum(array))

"""
    3. The knapsack problem. Given the weights and values of N items, put them in a 
    knapsack having capacity W so that 
    you maximize the value of the stored items. Items can be broken up.
"""

# W = 6
# weights = [1, 3, 3]
# values = [2, 3, 3]

W = 11
weights = [2, 1, 3, 4, 6]
values = [3, 2, 4, 3, 8]

"""
    4. 0-1 knapsack problem. Given the weights and values of N items, put them in a 
    knapsack having capacity W so that 
    you maximize the value of the stored items. Items cannot be broken up 
    (0-1 property).
"""


def knapsack_01_naive(W: int, weights: list, values: list, index: int) -> int:
    if index >= len(weights):
        # we're out of objects to consider :(
        return 0

    # calculate the value when we do not include the object in the knapsack
    exclude_value = knapsack_01_naive(W, weights, values, index + 1)

    include_value = 0
    if W - weights[index] >= 0:
        include_value = values[index] + knapsack_01_naive(W - weights[index], weights, values, index + 1)

    return max(exclude_value, include_value)


# index = 0 -> decide to include or exclude the first object
print(knapsack_01_naive(W, weights, values, 0))

"""
    5. Count in how many ways we can provide change to a given sum of money (N), 
    when provided infinite supplies of the 
    given coin denominations.

    e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can give 
    change in 4 ways (10, 5 + 5, 5 + 1 + ... and 1 + ... + 1)
"""

"""
    6. The checkerboard problem
   https://www.geeksforgeeks.org/gold-mine-problem
"""
