"""
Exponential search on a list sorted in ascending order
"""

from ex10_binary_search import binary_search_impl


def exponential_search(data: list, key):
    """
    Return an index of key in a sorted list, or -1 if not found
    """
    if len(data) == 0 or key < data[0] or key > data[-1]:
        return -1

    if data[0] == key:
        return 0

    # Find an interval that may contain the key: 1, 2, 4, 8, ...
    i = 1
    while i < len(data) and data[i] < key:
        i = i * 2

    # Search only the candidate interval, using the binary search helper.
    left = i // 2
    right = min(i, len(data) - 1)
    return binary_search_impl(data, key, left, right)


def test_exponential_search():
    assert exponential_search([], 10) == -1
    assert exponential_search([20], 20) == 0
    assert exponential_search([20], 10) == -1
    assert exponential_search([20], 30) == -1
    assert exponential_search([-10, 0, 20, 40], -10) == 0
    assert exponential_search([-10, 0, 20, 40], 40) == 3
    assert exponential_search([-10, 0, 20, 40], 10) == -1
    assert exponential_search([1, 2, 2, 2, 5], 2) in (1, 2, 3)

    data = list(range(1000))
    for i in range(len(data)):
        assert exponential_search(data, i) == i


if __name__ == "__main__":
    test_exponential_search()
    print("Exponential search tests passed.")
