"""
Merge sort: divide, recursively sort, then merge.

merge_sort(data) modifies the original list and returns that same list.
It is stable: equal elements retain their original relative order.

Assuming constant-time comparisons:
    Best/average/worst time: O(n log n)
    Auxiliary space:         O(n), including temporary lists
    Recursion depth:         O(log n)

Modifying the original list does NOT mean using constant auxiliary space:
this implementation creates copies of the two halves at every recursive call.
"""


def merge(left: list, right: list, destination: list):
    """
    Merge two sorted lists into destination and return destination.

    Preconditions:
        left and right are sorted in ascending order.
        destination is a different list from both left and right.
    The previous contents of destination are replaced.
    left and right are not modified.

    Time: O(len(left) + len(right)).
    """
    destination.clear()
    left_index = 0
    right_index = 0

    # At every step, destination contains the smallest elements processed
    # so far, in sorted order. Compare the next unused item from each half.
    while left_index < len(left) and right_index < len(right):
        # Take from the LEFT on a tie. Elements in the left half originally
        # came before elements in the right half, so this preserves stability.
        if left[left_index] <= right[right_index]:
            destination.append(left[left_index])
            left_index = left_index + 1
        else:
            destination.append(right[right_index])
            right_index = right_index + 1

    # One half is exhausted. The other half is already sorted, so append
    # its remaining elements without further comparisons.
    while left_index < len(left):
        destination.append(left[left_index])
        left_index = left_index + 1

    while right_index < len(right):
        destination.append(right[right_index])
        right_index = right_index + 1

    return destination


def merge_sort(data: list):
    """
    Sort data in ascending order and return the same list.
    """
    # Base case: an empty list or a one-element list is already sorted.
    if len(data) < 2:
        return data

    # 1. DIVIDE: slicing creates two new lists.
    middle = len(data) // 2
    left = data[:middle]
    right = data[middle:]

    # 2. CONQUER: recursively sort each half.
    merge_sort(left)
    merge_sort(right)

    # 3. COMBINE: both halves are now sorted, so we can merge them.
    merge(left, right, data)
    return data


if __name__ == "__main__":
    # First study merging on its own, before following the recursion.
    left = [1, 4, 7]
    right = [2, 4, 6]
    combined = []
    merge(left, right, combined)
    print("Left half:   ", left)
    print("Right half:  ", right)
    print("Merged list: ", combined)

    # Follow the recursive calls in the debugger, then watch the merges
    # as the calls return. No sorting takes place during the splitting step.
    numbers = [5, 2, 4, 2, 1, 6, 3]
    print("\nBefore sorting:", numbers)
    merge_sort(numbers)
    print("After sorting: ", numbers)
