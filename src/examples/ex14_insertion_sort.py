"""
Insertion sort and binary insertion sort.

Both functions sort the original list in ascending order and return that same
list. Both are stable: elements with equal keys keep their original order.

For these implementations, assuming constant-time comparisons:
    Best-case time:       O(n), when the list is already sorted
    Average/worst time:   O(n^2)
    Auxiliary space:     O(1)

Binary search reduces the comparisons needed to locate an insertion position.
It does not remove the need to shift elements to make room.

The original binary insertion example was adapted from:
https://www.geeksforgeeks.org/binary-insertion-sort/
(code contributed by Mohit Gupta_OMG). The version below uses iterative
search and explicit shifts to preserve stability and constant extra space.
"""


def insertion_sort(data: list):
    """
    Sort data in place using insertion sort; return the same list.
    """
    for i in range(1, len(data)):
        # The elements before index i are already sorted.
        # Save the current value before shifting any elements over it.
        value = data[i]
        j = i - 1

        # Move larger elements one position to the right to make room.
        # Do not move equal elements: this keeps the sort stable.
        while j >= 0 and data[j] > value:
            data[j + 1] = data[j]
            j = j - 1

        # Insert once, after all the necessary shifts have finished.
        data[j + 1] = value

    return data


def binary_search(arr: list, val, start: int, end: int):
    """
    Find an insertion position in an already sorted part of arr.

    start and end are inclusive bounds. Return the first position whose
    element is greater than val, or end + 1 if there is no such element.
    Thus, val is inserted AFTER all existing equal values, preserving stability.
    For an empty range (start > end), return start.

    The function does not modify arr. For a nonempty range of m elements,
    it uses O(log(m + 1)) comparisons and O(1) auxiliary space.
    """
    while start <= end:
        middle = (start + end) // 2

        if arr[middle] > val:
            # This position might work, but an earlier one might also work.
            end = middle - 1
        else:
            # arr[middle] <= val: insert after this element, even on a tie.
            start = middle + 1

    return start


def binary_insertion_sort(data: list):
    """
    Sort data in place using binary insertion sort; return the same list.
    """
    for i in range(1, len(data)):
        # As in ordinary insertion sort, the elements before i are sorted.
        value = data[i]

        # If value already follows the sorted prefix, no search is needed.
        # This check gives the algorithm linear time on already sorted input.
        if data[i - 1] <= value:
            continue

        position = binary_search(data, value, 0, i - 1)

        # Finding the position is logarithmic, but making room can be linear.
        # Shift from right to left so that no value is overwritten too soon.
        j = i
        while j > position:
            data[j] = data[j - 1]
            j = j - 1

        data[position] = value

    return data


if __name__ == "__main__":
    # Use copies so both algorithms receive the same starting list.
    numbers = [5, 2, 4, 2, 1]
    print("Original list:        ", numbers)

    ordinary = numbers.copy()
    insertion_sort(ordinary)
    print("Insertion sort:       ", ordinary)

    binary = numbers.copy()
    binary_insertion_sort(binary)
    print("Binary insertion sort:", binary)
