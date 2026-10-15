"""
Binary search: iterative and recursive implementations
"""


def binary_search_rec(data: list, key):
    """
    Return the index of key in a sorted list, or -1 if not found.

    The list must be sorted in ascending order. If key appears multiple
    times, any matching index may be returned.
    """
    return binary_search_impl(data, key, 0, len(data) - 1)


def binary_search_impl(data: list, key, left: int, right: int):
    """
    Search the inclusive interval [left, right] recursively.

    This helper is also used by the exponential search example.
    """
    if left > right:  # No candidates remain.
        return -1

    middle = (left + right) // 2
    if data[middle] == key:
        return middle
    elif data[middle] < key:
        return binary_search_impl(data, key, middle + 1, right)
    else:
        return binary_search_impl(data, key, left, middle - 1)


def binary_search_iter(data: list, key):
    """
    Return the index of key in a sorted list, or -1 if not found.
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2

        if data[middle] == key:
            return middle
        elif data[middle] < key:
            left = middle + 1  # Discard the left half (including middle).
        else:
            right = middle - 1  # Discard the right half (including middle).

    return -1


def test_binary_search():
    algorithms = [binary_search_iter, binary_search_rec]

    for search in algorithms:
        assert search([], 10) == -1
        assert search([20], 20) == 0
        assert search([20], 10) == -1
        assert search([-10, 0, 20, 40], -10) == 0
        assert search([-10, 0, 20, 40], 40) == 3
        assert search([-10, 0, 20, 40], 10) == -1  # Missing, inside range
        assert search([-10, 0, 20, 40], 100) == -1

        duplicates = [1, 2, 2, 2, 5]
        assert search(duplicates, 2) in (1, 2, 3)

        data = list(range(1000))
        for i in range(len(data)):
            assert search(data, i) == i


if __name__ == "__main__":
    test_binary_search()
    print("Binary search tests passed.")
