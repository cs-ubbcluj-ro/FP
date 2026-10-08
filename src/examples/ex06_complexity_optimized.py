import timeit

from examples.ex05_complexity import fibonacci_recursive, fibonacci_iterative

'''
    To speed up the recursive implementation, we use memoization to store interim results
'''
results = {0: 0, 1: 1}


def fibonacci_memoization(n):
    if n not in results:
        results[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return results[n]


dataList = []

def build_result_table():
    table = [f"{'Term':<6} {'Iterative':<14} {'Recursive':<14} {'Memoization':<14}"]
    for term in [10, 20, 30, 32, 34, 36]:
        # Iterative
        start_iter = timeit.default_timer()
        row = fibonacci_iterative(term)
        end_iter = timeit.default_timer()
        # Recursive
        start_rec = timeit.default_timer()
        row = fibonacci_recursive(term)
        end_rec = timeit.default_timer()
        # Recursive with memoization
        start_mem = timeit.default_timer()
        row = fibonacci_memoization(term)
        end_mem = timeit.default_timer()

        table.append(f"{term:<6} {end_iter - start_iter:<14.6f} {end_rec - start_rec:<14.6f} {end_mem - start_mem:<14.6f}")
    return "\n".join(table)


if __name__ == "__main__":
    print(build_result_table())

'''
    In case you cannot run the example, this is what it is supposed to look like:
    
    +------+-----------+-----------+-------------+
    | Term | Iterative | Recursive | Memoization |
    +------+-----------+-----------+-------------+
    | 10   | 0         | 0         | 0           |
    +------+-----------+-----------+-------------+
    | 20   | 0         | 3         | 0           |
    +------+-----------+-----------+-------------+
    | 30   | 0         | 345       | 0           |
    +------+-----------+-----------+-------------+
    | 32   | 0         | 912       | 0           |
    +------+-----------+-----------+-------------+
    | 34   | 0         | 2381      | 0           |
    +------+-----------+-----------+-------------+
    | 36   | 0         | 6215      | 0           |
    +------+-----------+-----------+-------------+

    NB!
    0 milliseconds is not really 0, it's just too short to measure accurately
'''
