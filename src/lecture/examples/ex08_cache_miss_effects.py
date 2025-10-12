import time
import random

"""
    Matrix size - increase this to see stronger effects
"""
N = 1_000

# Create a matrix (a list of Python lists)
A = [[random.random() for column in range(N)] for row in range(N)]

"""
    --- Row-major traversal ---
    This is done in the order in which the default Python implementation stores the lists
    (think of it as reading a book) 
"""
start = time.perf_counter()
s = 0.0
for i in range(N):
    row = A[i]
    for j in range(N):
        s += row[j]
end = time.perf_counter()
print(f"Row-major access: {end - start:.3f} s, sum={s:.2f}")

"""
    --- Column-major traversal ---
    This jumps between different memory addresses; this can cause the CPU caches to not hold the information the is 
     required next, making the CPU wait until data becomes available
    (think of it as reading a book, but having to flip between pages at the start of every paragraph)

    Hint: increase the size of N to see a more pronounced effect, and keep in mind that these things depend
    on the design of the CPU running them :) 
"""
start = time.perf_counter()
s = 0.0
for j in range(N):
    for i in range(N):
        s += A[i][j]
end = time.perf_counter()
print(f"Column-major access: {end - start:.3f} s, sum={s:.2f}")