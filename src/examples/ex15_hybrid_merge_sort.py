"""
Hybrid merge sort with binary insertion sort for short sublists.

A sublist of length <= cutoff is sorted by binary insertion sort. Larger
sublists are split recursively and then merged, just as in ordinary merge sort.
The sort modifies the original list, returns that same list, and is stable.

For a FIXED (does not depend on n) cutoff, assuming constant-time comparisons:
    Worst-case time: O(n log n)
    Auxiliary space: O(n)

The cutoff is a tuning parameter, not a universal optimal value. A very large
cutoff can make the algorithm quadratic: if cutoff >= n, the entire list is
sorted using binary insertion sort. cutoff = 1 gives ordinary merge sort.

This is a merge/insertion hybrid, not a full TimSort implementation: it does
not detect natural runs, schedule run-stack merges, or perform galloping.
"""

from ex14_insertion_sort import binary_insertion_sort
from ex15_merge_sort import merge


DEFAULT_CUTOFF = 16


def hybrid_merge_sort(data: list, cutoff: int = DEFAULT_CUTOFF):
    """
    Sort data in ascending order and return the same list.

    cutoff must be a positive integer. It is the largest sublist length
    handled directly by binary insertion sort.
    """
    # Validate once at the public entry point, rather than at every recursion.
    if type(cutoff) is not int:
        raise TypeError("cutoff must be an integer")
    if cutoff < 1:
        raise ValueError("cutoff must be at least 1")

    _hybrid_merge_sort(data, cutoff)
    return data


def _hybrid_merge_sort(data: list, cutoff: int):
    """
    Recursive helper; the public function has already checked cutoff.
    """
    if len(data) < 2:
        return

    # The only algorithmic change from merge sort: stop splitting early.
    # Binary insertion sort avoids further recursive calls and merge buffers
    # for this small sublist. It still needs shifts to make room for elements.
    if len(data) <= cutoff:
        binary_insertion_sort(data)
        return

    middle = len(data) // 2
    left = data[:middle]
    right = data[middle:]

    # Pass the SAME cutoff to both recursive calls.
    _hybrid_merge_sort(left, cutoff)
    _hybrid_merge_sort(right, cutoff)
    merge(left, right, data)


if __name__ == "__main__":
    numbers = [9, 4, 7, 3, 1, 8, 2, 6, 5, 0]
    print("Original list:", numbers)

    # Use 3 to see both algorithms on this small example. In the debugger,
    # watch the length-2 and length-3 sublists go to binary insertion sort.
    data = numbers.copy()
    hybrid_merge_sort(data, cutoff=3)
    print("Cutoff 3:    ", data)

    # Compare splitting down to single elements with using insertion sort
    # for the whole list. All cutoffs must produce the same sorted result.
    for cutoff in [1, 4, 16]:
        data = numbers.copy()
        hybrid_merge_sort(data, cutoff=cutoff)
        print("Cutoff", cutoff, "->", data)
