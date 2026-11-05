"""
Function calls: separate local bindings and returning to the caller.
Copy this file into https://pythontutor.com/visualize.html, or use the debugger.

1. Trace add_then_double(3, 4) first. Predict the result before running.
   At the deepest call, identify the caller, parameters, local values, and
   the statement that will continue when the function returns.
2. Trace fib(4). Each invocation has its own n, even though the name is shared.
   Which recursive call happens first? Which calls return immediately?

Expected results: 14 and 3.
Functions may calculate before a call, between calls, or after a call returns.
"""


def double(number: int) -> int:
    """Return 2 * number without changing any external state."""
    result = number * 2
    return result


def add_then_double(first: int, second: int) -> int:
    """Return 2 * (first + second); neither argument changes."""
    total = first + second  # This calculation happens BEFORE the next call.
    result = double(total)
    return result


def fib(n: int) -> int:
    """
    Return Fibonacci number n, with F(0) = 0 and F(1) = 1.
    Precondition: n is a non-negative integer.
    No external state is changed.
    This deliberately simple recursive algorithm is for tracing small inputs.
    """
    if n < 2:
        return n
    first = fib(n - 2)
    second = fib(n - 1)
    return first + second  # This addition waits for BOTH calls to return.


if __name__ == "__main__":
    print(add_then_double(3, 4))
    print(fib(4))  # Nine calls: small enough to trace by hand.
