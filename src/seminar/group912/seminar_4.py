"""
    Problem Solving Methods -- Divide & Conquer, Backtracking
"""
import random
from src.lecture.examples.ex14_insertion_sort import binary_insertion_sort

"""
    1. Implement an optimized version of the merge sort algorithm
        a. Implement Merge Sort + test function
        b. Use the insertion sorting algorithm with the binary search optimization found in the lecture examples
        c. Time the resulting version using the ex18_sort_comparison.py example
        d. Could merging be further improved using exponential search?
"""


def generate_random(lenght):
    numbers = []
    for i in range(lenght):
        numbers.append(random.randint(1, 1000))
    return numbers


def insertion_sort(data):
    for i in range(1, len(data)):
        j = i - 1
        key = data[i]
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def test_sort():
    for i in range(1000):
        n = random.randint(1, 1000)
        list1 = generate_random(n)
        list2 = list1[:]
        list3 = list1[:]
        sorted_list = merge_sort_optimized(list1)
        sorted_list1 = insertion_sort(list3)
        list2.sort()
        if sorted_list != list2:
            print("Sorting is not ok!")
        if sorted_list1 != list2:
            print("Sorting is not ok!")


def merge_sort_optimized(data) -> list:
    if len(data) <= 32:
        # return data
        # insertion_sort(data)
        return binary_insertion_sort(data)
    else:
        mid = len(data) // 2
        right = merge_sort_optimized(data[:mid])
        left = merge_sort_optimized(data[mid:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


test_sort()

"""
    2. Find the smallest number in a list using a recursive divide & conquer implementation. Return None for an empty 
    list. Implement the following variants:
        a. Chip & conquer
        b. Divide the list into halves
"""

"""
    3. Calculate the r-th root of a given number x with a given precision p
"""

"""
    4. Calculate the maximum subarray sum (elements of a subarray have consecutive indices in the parent array)
        a. Naive implementation
        b. Divide & conquer implementation
        c. Dynamic programming implementation (next week)

        e.g.
        for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    5. All permutations of the {0, 2, ..., n - 1} set (recursive implementation)
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


# bkt_rec([], 4)

"""
    6. Change the code above to work for the n-Queen problem
"""

"""
    7. A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and 
    exactly once in each column

    Generate all the N x N Latin squares for a given number N. 
"""

"""
    8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the 
    first row and first column are sorted.
"""
