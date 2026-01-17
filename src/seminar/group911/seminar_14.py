"""
Divide & conquer

Write a recursive Python function that uses divide & conquer to count how many even elements are
found on odd positions of a list of natural numbers.

    1. Divide the list into halves without using list slicing (use indices).
    2. Remove the recursive call by simulating the recursion using a stack.
    + write a test function

    [copy paste the code to https://codeshare.io/fp911]
"""


def cnt(lst, start, end):
    """
    n -> the algorithm's input size, here n = len(lst)

    Time complexity:
        T(n) -> the number of operations carried out by the algorithm

        T(1) = 1, basic case
        T(n) = 2 * T(n/2) + 1

    Extra-space complexity:
        = how much memory the algorithm needs, disregarding the original input

        T(1) = 1, basic case
        T(n) = T(n/2) + 1
             = T(n/4) + 1 + 1
             = ...
             = T(1) + 1 + ... + 1 # T(1) = 1, the sum 1 + ... + 1 has log_2(n+1) operands
        the algorithm has O(log_2(n)) extra-space complexity
    """
    if len(lst) == 0:  # not lst
        return 0
    if start == end:
        return start % 2 == 1 and lst[start] % 2 == 0
    mid = (start + end) // 2
    return cnt(lst, start, mid) + cnt(lst, mid + 1, end)


max_len = 0


def cnt2(lst):
    global max_len
    stack = [(0, len(lst) - 1)]
    res = 0
    while len(stack) > 0:
        max_len = max(len(stack), max_len)
        print(stack)
        start, end = stack.pop()
        if start == end:
            res += start % 2 == 1 and lst[start] % 2 == 0
        else:
            mid = (start + end) // 2
            stack.append((start, mid))
            stack.append((mid + 1, end))
    return res


cnt2([1, 2, 3, 4, 5, 6, 7, 8])


# check extra-space complexity empirically
# for i in range(10):
#     data = list(range(2 ** i))
#     max_len = 0
#     cnt2(data)
#     print(len(data), max_len)


def test():
    assert cnt([1, 2, 3, 4, 5, 6], 0, 5) == 3
    assert cnt([1, 3, 4, 6, 8, 9], 0, 5) == 1
    assert cnt2([1, 2, 3, 4, 5, 6]) == 3
    assert cnt2([1, 3, 4, 6, 8, 9]) == 1
    print("No errors :)")


"""
Dynamic programming

A stair can be climbed by going up 1, 2 or 3 steps at once. Determine in how many ways we can go up
a staircase of 10 stairs.

    Number of stairs:
        1 stair  -> 1 way
        2 stairs -> 2 ways (1+1, 2)
        3 stairs -> 4 ways (1+1+1, 1+2, 2+1, 3)
        4 stairs -> (1+3, 1+1+2, 2+2,1+1+1+1,1+2+1,2+1+1,3+1) 

"""


def naive_stairs(n: int) -> int:
    """
    Time complexity:
        T(n) = 3 * T(n-2) + 1 => O(3^n)
    Extra-space complexity:
        T(n) = T(n-1) + 1 => O(n)
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return naive_stairs(n - 3) + naive_stairs(n - 2) + naive_stairs(n - 1)


def ways_to_climb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


def count_ways_stairs(n):
    # Fenici Andra 913/2
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4

    a, b, c = 1, 2, 4

    for i in range(4, n + 1):
        current = a + b + c
        a = b
        b = c
        c = current

    return c


print(f"Result for 10 stairs: {count_ways_stairs(10)}")

"""
    Coin Change Problem - Find the fewest number of coins needed to make a specific total
    
    Example:
        We have coins {1, 3, 4}
        We want to make a total of 8 (we need 2 coins of 4)
        
    Naive version:
        coins(n) = coins(n - 1) + coins(n - 3) + coins(n - 4) 
"""
