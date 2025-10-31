data = {0: 0, 1: 1}


def fib_rec(n: int) -> int:
    if n not in data:
        data[n] = fib_rec(n - 2) + fib_rec(n - 1)
    return data[n]


print(fib_rec(10))
