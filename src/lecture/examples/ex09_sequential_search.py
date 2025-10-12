def search_iter(data: list, key):
    for i in range(len(data)):
        if data[i] == key:
            return i
    return -1


def search_rec(data: list, key, pos: int = 0):
    if len(data) > 997:
        # The initial execution of the current module and
        # initial method call are already on the stack, so we have fewer than
        # 1000 recursive calls available in the default Python implementation ;)
        raise ValueError("Will overflow the Python stack")

    if 0 > pos or pos >= len(data):
        return -1
    if data[pos] == key:
        return key
    return search_rec(data, key, pos + 1)
