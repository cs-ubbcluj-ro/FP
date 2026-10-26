"""
Quicksort with a last-element pivot.

Start with partition(), then quick_sort() and its recursive helper. These
follow the lecture's divide/conquer/combine description: partition puts the
pivot in its final position, then the two remaining subranges are sorted.

The public sorting functions modify the original list and return that list.
This sort is NOT stable: swaps can change the order of equal elements.

Assuming constant-time comparisons:
    Best/average time: O(n log n)
    Worst-case time:   O(n^2)
    Recursive stack:   O(log n) for balanced splits; O(n) in the worst case
The average assumes a uniformly random permutation of distinct keys.
Partitioning itself uses O(1) auxiliary space and creates no list slices.

Sorted, reverse-sorted, and all-equal lists produce worst-case partitions
with this pivot rule. Large inputs of these kinds can exceed Python's
recursion limit. The optional iterative version below avoids that recursion
limit, but retains the same worst-case running time.

quick_sort_iterative_fast adds median-of-three pivot selection, two-way
partitioning, insertion sort for short ranges, and a bounded work stack.
It is an extension; partition() still illustrates the lecture algorithm.
"""


def partition(data: list, low: int, high: int):
    """
    Partition data[low..high] and return the pivot's final index.

    Bounds are inclusive; require 0 <= low <= high < len(data).
    On return, elements before the pivot in this range are <= the pivot,
    and elements after it are > the pivot. Elements outside the range are
    unchanged. Time is O(high - low + 1); auxiliary space is O(1).
    """
    pivot = data[high]
    boundary = low

    # Before examining data[current]:
    #   low .. boundary - 1       contains values <= pivot
    #   boundary .. current - 1   contains values > pivot
    #   current .. high - 1       has not been examined
    # The pivot stays at high until the scan finishes.
    for current in range(low, high):
        if data[current] <= pivot:
            data[boundary], data[current] = data[current], data[boundary]
            boundary = boundary + 1

    # Place the pivot between the two groups. Its position is now final:
    # later calls will sort only the elements before and after it.
    data[boundary], data[high] = data[high], data[boundary]
    return boundary


def quick_sort_recursive(data: list):
    """
    Sort data recursively in ascending order; return the same list.
    """
    _quick_sort(data, 0, len(data) - 1)
    return data


def _quick_sort(data: list, low: int, high: int):
    """
    Recursively sort a range with inclusive bounds.
    """
    # Base case: the range contains zero or one element.
    if low >= high:
        return

    # 1. DIVIDE: partition and put the pivot in its final position.
    pivot_index = partition(data, low, high)

    # 2. CONQUER: sort both remaining ranges, excluding the pivot.
    # Passing indices avoids copying the sublists.
    _quick_sort(data, low, pivot_index - 1)
    _quick_sort(data, pivot_index + 1, high)

    # 3. COMBINE: no merge is needed. The left range, pivot, and right range
    # are already in the correct relative positions in the original list.


def quick_sort_unoptimized(data: list):
    """
    Optional extension: the same partitioning, using an explicit work stack.

    Study this after the recursive version. Each pair stores the inclusive
    bounds of one range still to sort. Worst-case auxiliary space is O(n);
    avoiding recursive calls alone does not guarantee an O(log n) stack.
    """
    if len(data) < 2:
        return data

    pending = [(0, len(data) - 1)]
    while len(pending) > 0:
        low, high = pending.pop()
        pivot_index = partition(data, low, high)

        # Push the right range first so the left is processed next, just as
        # in the recursive version. Skip ranges of length zero or one.
        if pivot_index + 1 < high:
            pending.append((pivot_index + 1, high))
        if low < pivot_index - 1:
            pending.append((low, pivot_index - 1))

    return data


def quick_sort_optimized(data: list, cutoff: int = 16):
    """
    Sort in place using median-of-three pivots and two-way partitioning.

    Returns the same list. This version is not stable.
    Small ranges use insertion sort; cutoff must be a positive integer.
    Expected time on random input: O(n log n); worst case: O(n^2).

    For a fixed cutoff, the explicit work stack uses O(log n) space.
    No recursive calls or list slices are used.
    """
    if type(cutoff) is not int or cutoff < 1:
        raise ValueError("cutoff must be a positive integer")
    if len(data) < 2:
        return data

    pending = [(0, len(data) - 1)]
    while pending:
        low, high = pending.pop()
        while high - low + 1 > cutoff:
            middle = (low + high) // 2
            # Choose the median VALUE of the first, middle, and last items.
            # This avoids the extreme pivot of ordinary monotone input.
            first, center, last = data[low], data[middle], data[high]
            if center < first:
                first, center = center, first
            if last < center:
                center = last
                if center < first:
                    center = first
            pivot = center

            # Hoare-style scan: move small values left and large values right.
            # Unlike Lomuto partitioning, this does not place one pivot item
            # at a final index. Both resulting ranges still need sorting.
            left, right = low, high
            while left <= right:
                while data[left] < pivot:
                    left += 1
                while pivot < data[right]:
                    right -= 1
                if left <= right:
                    data[left], data[right] = data[right], data[left]
                    # Advance even on equal values, so duplicates cannot stall.
                    left += 1
                    right -= 1

            # Defer the larger range and process the smaller immediately.
            # This bounds the explicit stack by O(log n), even on bad splits.
            if right - low < high - left:
                if left < high:
                    pending.append((left, high))
                high = right
            else:
                if low < right:
                    pending.append((low, right))
                low = left

        # Insertion sort avoids partition overhead on a short range.
        for index in range(low + 1, high + 1):
            value = data[index]
            position = index
            while position > low and value < data[position - 1]:
                data[position] = data[position - 1]
                position -= 1
            data[position] = value

    return data


if __name__ == "__main__":
    # Observe one partition first. The two sides need not yet be sorted.
    numbers = [4, 2, 5, 1, 3]
    print("Before partition:", numbers)
    pivot_index = partition(numbers, 0, len(numbers) - 1)
    print("After partition: ", numbers)
    print("Pivot index:     ", pivot_index)
    print("Left side:       ", numbers[:pivot_index])
    print("Pivot:           ", numbers[pivot_index])
    print("Right side:      ", numbers[pivot_index + 1:])

    numbers = [5, 2, 4, 2, 1, 6, 3]
    print("\nBefore sorting:", numbers)
    quick_sort_recursive(numbers)
    print("After sorting: ", numbers)

    # In the debugger, compare this with already sorted or all-equal input.
    # Predict pivot_index and the next two range sizes after each partition.
