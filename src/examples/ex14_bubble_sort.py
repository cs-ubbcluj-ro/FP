"""
Bubble sort: repeatedly exchange adjacent items that are out of order.

Stable, in-place, O(1) auxiliary space. Best time O(n) for sorted input;
average and worst time O(n^2), assuming constant-time comparisons.
"""


def bubble_sort(data: list):
    """
    Sort data in ascending order and return the same list.
    """

    # After each pass, the largest remaining item reaches the right end.
    # The suffix beyond end is already in its final sorted position.
    for end in range(len(data) - 1, 0, -1):
        swapped = False
        for index in range(end):
            # Strict comparison preserves the relative order of equal items.
            if data[index + 1] < data[index]:
                data[index], data[index + 1] = data[index + 1], data[index]
                swapped = True
        if not swapped:
            # No adjacent inversion remains: the entire list is sorted.
            break
    return data


if __name__ == "__main__":
    numbers = [5, 2, 4, 2, 1, 6, 3]
    print("Before sorting:", numbers)
    bubble_sort(numbers)
    print("After sorting: ", numbers)
