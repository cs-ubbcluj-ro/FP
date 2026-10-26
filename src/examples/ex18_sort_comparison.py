"""
Compare sorting implementations on three input patterns.

Each table reports median elapsed time in milliseconds. Every algorithm gets
an independent copy of exactly the same input for each size and trial.
Data generation, copying, and correctness checking are outside the timer.

Python's built-in list.sort() is an optimized runtime implementation. These
measurements compare implementations, not just abstract algorithms.
"""

from random import Random
from statistics import median
from time import perf_counter

from ex14_bubble_sort import bubble_sort
from ex14_insertion_sort import insertion_sort, binary_insertion_sort
from ex15_merge_sort import merge_sort
from ex15_hybrid_merge_sort import hybrid_merge_sort
from ex16_quick_sort import quick_sort_unoptimized, quick_sort_optimized

DATA_SIZES = [64, 128, 256, 512, 1024, 2048, 4096, 8192]
REPEATS = 3
HYBRID_CUTOFF = 16
RANDOM_SEED = 2026


def already_sorted_data(data_size):
    return list(range(data_size))


def sorted_in_reverse_data(data_size):
    # Use the same values as the ascending and random patterns.
    return list(range(data_size - 1, -1, -1))


def random_data(data_size, rng=None):
    if rng is None:
        rng = Random(RANDOM_SEED)
    data = list(range(data_size))
    rng.shuffle(data)
    return data


def python_sort(data):
    """
    Use Python's default mutating sort, matching the other interfaces.
    """
    data.sort()
    return data


def get_sort_functions(cutoff=HYBRID_CUTOFF):
    # This small wrapper lets the benchmark call every function with one list.
    def hybrid_sort(data):
        return hybrid_merge_sort(data, cutoff=cutoff)

    return [
        ("Bubble sort", bubble_sort),
        ("Insertion sort", insertion_sort),
        ("Binary insertion sort", binary_insertion_sort),
        ("Merge sort", merge_sort),
        ("Hybrid merge (insert sort cutoff=" + str(cutoff) + ")", hybrid_sort),
        ("Quicksort (lecture notes)", quick_sort_unoptimized),
        ("Quicksort (optimized)", quick_sort_optimized),
        # ("TimSort (in Python)", tim_sort_rpython),
        ("list.sort() (in C)", python_sort),
    ]


def test_sorts():
    """
    Quick correctness checks before measuring. Timing is tested separately.
    """
    rng = Random(RANDOM_SEED)
    examples = [
        [], [1], [2, 1], [1, 1, 1], [3, -1, 3, 0, -1],
        already_sorted_data(100), sorted_in_reverse_data(100),
        random_data(100, rng),
        [rng.randrange(10) for _ in range(257)],
    ]
    for name, sort_function in get_sort_functions():
        for original in examples:
            data = original.copy()
            sort_function(data)
            if data != sorted(original):
                raise AssertionError(name + " produced an incorrect result")


def print_table(data_sizes, results):
    """
    Print aligned columns using only ordinary strings and format specs.
    """
    header = ["Algorithm / size"] + [str(size) for size in data_sizes]
    rows = [header]
    for name, times in results:
        # Fractional milliseconds keep small timings from becoming integer zero.
        rows.append([name] + [f"{elapsed:.4f}" for elapsed in times])

    widths = []
    for column in range(len(header)):
        widths.append(max(len(row[column]) for row in rows))

    separator = "-+-".join("-" * width for width in widths)
    for index, row in enumerate(rows):
        cells = [row[0].ljust(widths[0])]
        for column in range(1, len(row)):
            cells.append(row[column].rjust(widths[column]))
        print(" | ".join(cells), flush=True)
        if index == 0:
            print(separator, flush=True)


def sort_test(data_sizes=None, repeats=REPEATS, cutoff=HYBRID_CUTOFF):
    """
    Print one timing table for each of the three existing input patterns.
    """
    if data_sizes is None:
        data_sizes = DATA_SIZES
    if type(repeats) is not int or repeats < 1:
        raise ValueError("repeats must be a positive integer")
    if type(cutoff) is not int or cutoff < 1:
        raise ValueError("cutoff must be a positive integer")
    if any(type(size) is not int or size < 0 for size in data_sizes):
        raise ValueError("data sizes must be nonnegative integers")

    rng = Random(RANDOM_SEED)
    sort_functions = get_sort_functions(cutoff)
    patterns = [
        ("Already sorted", already_sorted_data),
        ("Random order", random_data),
        ("Sorted in reverse", sorted_in_reverse_data),
    ]
    print(f"Median of {repeats} trials; times in milliseconds.", flush=True)
    print("Copies and correctness checks are not timed.", flush=True)

    for pattern_name, generator in patterns:
        print("\n" + pattern_name + " (calculating...)", flush=True)
        results = [(name, []) for name, function in sort_functions]

        for size in data_sizes:
            samples = [[] for name, function in sort_functions]
            for trial in range(repeats):
                if generator is random_data:
                    original = random_data(size, rng)
                else:
                    original = generator(size)
                expected = sorted(original)

                for index, (name, sort_function) in enumerate(sort_functions):
                    data = original.copy()
                    start = perf_counter()
                    sort_function(data)
                    elapsed_ms = (perf_counter() - start) * 1000

                    # A fast but incorrect sort must not enter the results table.
                    if data != expected:
                        raise AssertionError(name + " produced an incorrect result")
                    samples[index].append(elapsed_ms)

            for index in range(len(sort_functions)):
                results[index][1].append(median(samples[index]))

        print_table(data_sizes, results)

    print("\nExamine the source code for the Quicksort implementations.")
    print("Python's built-in sort benefits from its optimized runtime implementation.")


if __name__ == "__main__":
    test_sorts()
    sort_test()
