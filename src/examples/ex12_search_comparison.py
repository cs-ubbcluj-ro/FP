"""
Compare search runtimes

Each table shows the time per search, in microseconds (smaller is faster).
List creation and table formatting are NOT part of the measurements.

NB! Since O(logn) search algorithms are very fast, we use several runs to improve the consistency of the reported
results
"""

import timeit

from ex09_sequential_search import search_iter
from ex10_binary_search import binary_search_iter, binary_search_rec
from ex11_exponential_search import exponential_search


def generate_list(length: int):
    """
    Generate a sorted list of even numbers: [0, 2, 4, ..., 2*(n-1)].

    The gaps let us search for a missing key *inside* the list's range.
    """
    return list(range(0, 2 * length, 2))


def measure_search(algorithm, data: list, key):
    """
    Return the best observed time per search, in microseconds.

    Fast algorithms need many repetitions to be measured reliably.
    We estimate a suitable repetition count, then repeat the timing.
    """
    timer = timeit.Timer(lambda: algorithm(data, key))

    # Estimate the cost of one call using a short preliminary run.
    initial_time = timer.timeit(number=10)
    time_per_call = initial_time / 10

    # Aim for roughly 20 ms per measurement; limit the repetition count.
    runs = max(1, min(100_000, int(0.02 / max(time_per_call, 1e-9))))

    timings = timer.repeat(repeat=5, number=runs)
    return min(timings) / runs * 1_000_000


def make_table(headers: list, rows: list):
    """
    Build a plain-text table with aligned columns
    """
    all_rows = [headers] + rows
    widths = []

    for column in range(len(headers)):
        widths.append(max(len(str(row[column])) for row in all_rows))

    def format_row(row):
        # Algorithm names are left-aligned; numerical columns right-aligned.
        cells = [str(row[0]).ljust(widths[0])]
        for i in range(1, len(row)):
            cells.append(str(row[i]).rjust(widths[i]))
        return " | ".join(cells)

    separator = "-+-".join("-" * width for width in widths)
    lines = [format_row(headers), separator]
    for row in rows:
        lines.append(format_row(row))
    return "\n".join(lines)


def build_result_table(algorithms: list, list_lengths: list, case: str = "middle"):
    """
    Return a formatted runtime table for one search scenario
    """
    headers = ["Algorithm / n"] + [f"{n:,}" for n in list_lengths]
    results = [[algorithm.__name__] for algorithm in algorithms]

    for length in list_lengths:
        data = generate_list(length)
        if case == "first":
            key = data[0]
        elif case == "middle":
            key = data[length // 2]
        elif case == "last":
            key = data[-1]
        elif case == "missing":
            key = data[-1] - 1  # Odd number, inside the sorted value range
        else:
            raise ValueError("Unknown search scenario: " + case)

        for row, algorithm in zip(results, algorithms):
            elapsed = measure_search(algorithm, data, key)
            row.append(f"{elapsed:.3f}")

    return make_table(headers, results)


if __name__ == "__main__":
    algorithms = [search_iter, binary_search_iter, binary_search_rec,
                  exponential_search]
    list_lengths = [10_000, 20_000, 40_000, 80_000, 160_000]

    print("Search time per call (microseconds; lower is better)")
    for case in ["first", "middle", "last", "missing"]:
        print("\nSearch scenario:", case)
        print(build_result_table(algorithms, list_lengths, case))
