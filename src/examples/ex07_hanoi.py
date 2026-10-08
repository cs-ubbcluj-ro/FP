import timeit


def hanoi(n, x, y, z):
    """
    n - number of disks on the x stick
    x - source Stick
    y - destination stick
    z - intermediate stick
    """
    if n == 1:
        return
    hanoi(n - 1, x, z, y)
    hanoi(n - 1, z, y, x)


def hanoi_verbose(n, x, y, z):
    """
    n - number of disks on the x stick
    x - source Stick
    y - destination stick
    z - intermediate stick
    """
    if n == 1:
        print("Disk 1 from ", x, " to ", y)
        return
    hanoi(n - 1, x, z, y)
    print("Disk ", n, " from ", x, " to ", y)
    hanoi(n - 1, z, y, x)


def build_result_table():
    table = [f"{'disks':<6} {'seconds':<14}"]
    for term in range(10, 26):
        t1 = timeit.default_timer()
        hanoi(term, "X", "Y", "Z")
        t2 = timeit.default_timer()
        table.append(f"{term:<6} {t2 - t1:<14.6f}")
    return "\n".join(table)


print(build_result_table())

'''
    In case you cannot run the example, this is what it is supposed to look like:
    
    +-------+-------------+
    | Disks | Miliseconds |
    +-------+-------------+
    | 10    | 0           |
    +-------+-------------+
    | 11    | 0           |
    +-------+-------------+
    | 12    | 1           |
    +-------+-------------+
    | 13    | 1           |
    +-------+-------------+
    | 14    | 3           |
    +-------+-------------+
    | 15    | 5           |
    +-------+-------------+
    | 16    | 10          |
    +-------+-------------+
    | 17    | 19          |
    +-------+-------------+
    | 18    | 39          |
    +-------+-------------+
    | 19    | 76          |
    +-------+-------------+
    | 20    | 154         |
    +-------+-------------+
    | 21    | 312         |
    +-------+-------------+
    | 22    | 614         |
    +-------+-------------+
    | 23    | 1223        |
    +-------+-------------+
    | 24    | 2440        |
    +-------+-------------+
    | 25    | 4891        |
    +-------+-------------+

    NB!
    0 milliseconds is not really 0, it's just too short to measure accurately
'''
