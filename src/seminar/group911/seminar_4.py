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


# print(sorted([4, 3, 2, 1]))
# x = sorted
# print(x)
#
# x = 5
# print(x([4, 3, 2, 1]))


# 1. Implement merge sort
def merge(l1: list, l2: list) -> list:
    l = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1

    while i < len(l1):
        l.append(l1[i])
        i += 1
    while j < len(l2):
        l.append(l2[j])
        j += 1

    return l


def mergesort_better(l: list) -> list:
    # if len(l) == 1:
    #     return l
    if len(l) <= 32:
        return binary_insertion_sort(l)
    mid = len(l) // 2
    left = mergesort_better(l[:mid])
    right = mergesort_better(l[mid:])

    return merge(left, right)


def test_mergesort():
    for i in range(1, 1000):
        n = random.randint(1, 1000)
        arr = random.choices(range(1, 1_000), k=n)
        arr_copy = arr[:]
        arr = mergesort_better(arr)
        arr_copy.sort()
        if arr != arr_copy:
            print("The sorting is incorrect.")


# test_mergesort()

data = list(range(10, 1, -1))  # the right side of range is excluded
print(data)
print(sorted(data))
print(data)
data.sort(reverse=True)
print(data)

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
