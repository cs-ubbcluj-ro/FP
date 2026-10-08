"""
Memory access order: equal complexity, potentially different running times.

We store a square matrix in ONE flat array, with its rows next to each other.
Unlike a list of lists, array('d') stores the numeric values themselves in a
contiguous buffer. The code 'd' means double-precision floating-point numbers.
We access it through a memoryview: slicing a view does NOT copy the numbers.

For a 3 x 3 matrix, row traversal visits indices:
    0, 1, 2,  3, 4, 5,  6, 7, 8
Column traversal visits indices:
    0, 3, 6,  1, 4, 7,  2, 5, 8

A CPU cache holds recently accessed memory in small blocks (cache lines).
Reading neighbours often lets us reuse values already fetched together.
Jumping between rows can reduce that reuse and make prefetching less effective.

This is a memory-locality demonstration, NOT a measurement of cache misses.
Python interpreter overhead, address translation, prefetching, and scheduling
also affect the timings. A small difference, or a reversed result, is possible.
Directly counting cache misses requires hardware performance counters.

References:
https://docs.python.org/3/library/array.html
https://docs.python.org/3/library/time.html#time.perf_counter
"""

from array import array
from statistics import median
from time import perf_counter

# Start with these sizes; remove 4096 for a smaller memory footprint.
# A 4096 x 4096 array uses about 128 MiB when each element occupies 8 bytes.
# Larger arrays take more time and memory; they do not guarantee a bigger gap.
SIZES = [256, 1024, 2048, 4096]
REPEATS = 4  # Even: each traversal runs first equally often.


def sum_in_order(data, size, start_step, element_step):
    """
    Sum a flat square matrix through a memoryview in the specified order.

    Preconditions: data is a 1-D memoryview of doubles, size > 0,
    and len(data) == size * size.
    For rows:    start_step = size, element_step = 1.
    For columns: start_step = 1,    element_step = size.

    start_step moves between the starting indices of rows or columns.
    element_step moves between elements within one row or column.

    Both traversals execute this SAME code. Only the two step values change.
    Each reads size * size elements and makes size calls to sum().
    In CPython, built-in sum() avoids a Python loop iteration per element,
    making memory access costs less hidden by interpreter overhead.
    """
    total = 0.0
    for line in range(size):
        start = line * start_step
        stop = start + size * element_step
        # The third slice value is the step between selected elements.
        # This creates a VIEW of one row or column, not a new numeric array.
        # As with list slices, a stop beyond the end is safely clipped.
        values = data[start:stop:element_step]
        total += sum(values)
    return total


def measure(data, size, start_step, element_step):
    """
    Time only the traversal, then check its result outside the timed region.
    """
    start = perf_counter()
    total = sum_in_order(data, size, start_step, element_step)
    elapsed = perf_counter() - start

    # The demonstration array contains only 1.0, so its sum is known exactly
    # for the sizes used here. Different addition orders cannot change it.
    assert total == size * size
    return elapsed


def compare_traversals(size, repeats):
    """
    Return buffer size and median traversal times for one matrix size.
    """
    assert size > 0
    assert repeats > 0 and repeats % 2 == 0

    # Allocation and initialisation are NOT part of the measured traversal.
    # Repeating a one-element array allocates a flat buffer of numeric values.
    numbers = array('d', [1.0]) * (size * size)
    memory_mib = len(numbers) * numbers.itemsize / (1024 * 1024)
    data = memoryview(numbers)
    # A memoryview refers to the existing buffer; it does not duplicate it.
    # Slicing numbers directly would copy data and spoil this comparison.

    # Run both paths once before collecting measurements. This reduces some
    # first-run effects; it does NOT make the whole array fit in CPU cache,
    # flush the caches, or guarantee identical cache contents before each run.
    sum_in_order(data, size, size, 1)
    sum_in_order(data, size, 1, size)

    row_times = []
    column_times = []
    for trial in range(repeats):
        # Alternate the order so that neither traversal always runs first.
        if trial % 2 == 0:
            row_times.append(measure(data, size, size, 1))
            column_times.append(measure(data, size, 1, size))
        else:
            column_times.append(measure(data, size, 1, size))
            row_times.append(measure(data, size, size, 1))

    # The median summarises the trials without letting one unusually slow
    # trial dominate the result. It does not eliminate measurement noise.
    return memory_mib, median(row_times), median(column_times)


def main():
    print("Same array, same loop body, different memory access order")
    print(f"Median of {REPEATS} trials per traversal; times are in seconds.")
    print()
    print(f"{'Size':>7} {'Buffer MiB':>12} {'Rows (s)':>12} "
          f"{'Columns (s)':>12} {'Column/row':>12}")

    for size in SIZES:
        memory_mib, row_time, column_time = compare_traversals(size, REPEATS)
        ratio = column_time / row_time
        print(f"{size:>7} {memory_mib:>12.1f} {row_time:>12.6f} "
              f"{column_time:>12.6f} {ratio:>11.2f}x", flush=True)

    print()
    print("Column/row > 1 means column traversal took longer.")
    print("Both traversals take Theta(size squared) time and constant auxiliary space.")
    print("If n is the total number of elements, both take Theta(n) time.")
    print("The matrix itself occupies Theta(size squared) space.")
    print("Timings illustrate locality effects; they do not count cache misses.")


# Importing the file defines the functions without allocating a large array
# or starting the benchmark.
if __name__ == '__main__':
    main()
