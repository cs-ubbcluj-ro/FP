"""
    Dynamic programming

    What to know for the written exam ... and beyond?
        1. Determine the overlapping subproblems
            => write in your own words, use a math formula
        2. Memoization - we store the solutions of already solved
        subproblems so that we can recall them later at O(1) speed
            => in DP, we solve the problem bottom-up, from the base case
            to the complex, "big problem"
        3. Principle of optimality => the solutions of the subproblems are
        full solutions for those given cases.
"""

"""
    1. Calculating the n-th term of the Fibonacci sequence
"""

"""
    2. Calculate the maximum subarray sum (subarray = elements having continuous indices)
"""
array = [2, -3, -1, 3, 4, -3, -1, 1, 1, 3, -4, 2, 3, -1, 5]


# print(sum(array[3:]))

def max_subarray_sum(array: list) -> int:
    current_max = array[0]
    global_max = array[0]

    for i in range(1, len(array)):
        if current_max > 0:
            # we extend the existing subarray with array[i]
            current_max = current_max + array[i]
        else:
            # start a new array here
            current_max = array[i]
        # if current_max > global_max:
        #     global_max = current_max
        global_max = max(global_max, current_max)

    return global_max


print(max_subarray_sum(array))

"""
    3. The knapsack problem. Given the weights and values of N items, 
    put them in a knapsack having capacity W so that 
    you maximize the value of the stored items. Items can be broken up.
"""

"""
    4. 0-1 knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that 
    you maximize the value of the stored items. Items cannot be broken up (0-1 property).
"""

# counterexample for Greedy
W = 6  # total weight that can be fit in the knapsack
values = [3, 3, 2]  # object values
weights = [3, 3, 1]  # object weights corresponding to the values

W = 11  # total weight that can be fit in the knapsack
values = [2, 1, 5, 4, 8]  # object values
weights = [1, 2, 3, 5, 6]  # object weights corresponding to the values


def knapsack_01_naive(W: int, weights: list, values: list, index: int) -> int:
    if index >= len(weights):
        # We have run out of objects
        return 0

    exclude_value = knapsack_01_naive(W, weights, values, index + 1)

    include_value = 0
    if W - weights[index] >= 0:
        include_value = values[index] + knapsack_01_naive(W - weights[index], weights, values, index + 1)

    return max(exclude_value, include_value)


print(knapsack_01_naive(W, weights, values, 0))

"""
    5. Count in how many ways we can provide change to a given sum 
    of money (N), when provided infinite supplies of the 
    given coin denominations.

    e.g. Let's say N = 10, and we have coins of values (1, 5, 10); 
    we can give 
    change in 4 ways (10, 5 + 5, 5 + 1 + ... and 1 + ... + 1)
"""

"""
    6. The checkerboard problem
   https://www.geeksforgeeks.org/gold-mine-problem
"""
