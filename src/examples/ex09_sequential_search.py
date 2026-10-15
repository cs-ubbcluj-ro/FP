"""
Sequential search: iterative and recursive implementations
"""


def search_iter(data: list, key):
    """
    Return the index of the first occurrence of key, or -1 if absent
    """
    for i in range(len(data)):
        if data[i] == key:
            return i
    return -1


def search_rec(data: list, key, pos: int = 0):
    """
    Return the index of the first occurrence of key, searching from pos.

    This implementation uses one recursive call for each examined element.
    Large lists may therefore exceed Python's recursion limit.
    """
    if pos < 0 or pos >= len(data):
        return -1

    if data[pos] == key:
        return pos  # Return the position, not the value!

    return search_rec(data, key, pos + 1)


def test_sequential_search():
    # Values are deliberately different from indices.
    algorithms = [search_iter, search_rec]

    for search in algorithms:
        assert search([], 10) == -1
        assert search([20], 20) == 0
        assert search([20], 10) == -1
        assert search([10, 20, 30], 20) == 1
        assert search([10, 20, 30], 99) == -1
        assert search([10, 20, 30], 30) == 2
        assert search([5, 7, 5], 5) == 0  # First occurrence


if __name__ == "__main__":
    test_sequential_search()
    print("Sequential search tests passed.")
