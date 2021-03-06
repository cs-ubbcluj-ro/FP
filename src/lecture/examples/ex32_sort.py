"""
Created on Dec 20, 2016

@author: Arthur
"""
from random import *
from datetime import *
from texttable import *


def BC(dataSize):
    result = list(range(0, dataSize))
    return result


def WC(dataSize):
    result = list(range(dataSize, 0, -1))
    return result


def AC(dataSize):
    result = list(range(0, dataSize))
    shuffle(result)
    return result


'''
    Simplest implementation of BS. No optimization
'''


def bubble_sort_no_opt(data):
    done = False
    while not done:
        done = True
        for i in range(0, len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                done = False


'''
    BS optimized knowing that the largest value in ascending sort takes its place after the first iteration
'''


def bubble_sort_opt(data):
    done = False
    n = len(data) - 1
    while not done:
        done = True
        i = 0
        while i < n:
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                done = False
            i += 1
        n -= 1


'''
    Further optimization of BS, when we realize that all elements that come AFTER the last swap are already sorted
'''


def bubble_sort_opt_n(data):
    n = len(data) - 1
    while n > 0:
        newn = 0
        i = 0
        while i < n:
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                newn = i
            i += 1
        n = newn


'''
    Insertion sort. Another O(n^2) complexity algorithm 
'''


def insert_sort(data):
    for i in range(1, len(data)):
        val = data[i]
        j = i - 1
        while (j >= 0) and (data[j] > val):
            data[j + 1] = data[j]
            j = j - 1
            data[j + 1] = val
    return data


'''
    Merge sort. An O(n*log(n)) sort
'''


def merge_sort(l):
    if len(l) < 2:
        return l

    mid = len(l) // 2
    leftHalf = l[:mid]
    rightHalf = l[mid:]
    merge_sort(leftHalf)
    merge_sort(rightHalf)
    merge(leftHalf, rightHalf, l)


def merge(l1, l2, lrez):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i = i + 1
        else:
            l.append(l2[j])
            j = j + 1
    while i < len(l1):
        l.append(l1[i])
        i = i + 1
    while j < len(l2):
        l.append(l2[j])
        j = j + 1
    lrez.clear()
    lrez.extend(l)


def test_sorts():
    l = list(range(100, 0, -1))
    bubble_sort_no_opt(l)
    assert l == list(range(1, 101))

    l.reverse()
    bubble_sort_opt(l)
    assert l == list(range(1, 101))

    l.reverse()
    bubble_sort_opt_n(l)
    assert l == list(range(1, 101))

    l.reverse()
    insert_sort(l)
    assert l == list(range(1, 101))

    l.reverse()
    merge_sort(l)
    assert l == list(range(1, 101))


test_sorts()

'''
    Utility function to convert a timedelta into a number of miliseconds
'''


def millis_interval(start, end):
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return int(millis)


'''
    And here we build our experiment

        data_generators - Change the functions that build the data set to be sorted
        sort_functions  - What functions will do the actual sort
        data_sizes      - What are the data sizes to be sorted
'''


def sort_test():
    """
    Generator functions for best case, average case and worst case
    """
    data_generators = [BC, AC, WC]

    '''
    Sorting functions to employ
    '''
    sort_functions = [bubble_sort_no_opt, bubble_sort_opt, bubble_sort_opt_n, insert_sort, merge_sort, sorted]

    '''
    Data sizes that will be sorted
    '''
    data_sizes = [64, 128, 256, 512, 1024, 2048, 4096]

    '''
    Do the sort and build the result table dynamically
    '''
    for generator in data_generators:
        print("Current data: " + generator.__name__)
        t = Texttable()
        t.add_row(['Functions/size'] + data_sizes)
        for sort_function in sort_functions:
            row = [sort_function.__name__]
            for size in data_sizes:
                data = generator(size)
                t1 = datetime.now()
                sort_function(data)
                t2 = datetime.now()
                row = row + [millis_interval(t1, t2)]
            t.add_row(row)
        print(t.draw())


sort_test()

'''
    In case you cannot run the program, the expected (~) results are below

Current data: BC
+--------------------+----+-----+-----+-----+------+------+------+
| Functions/size     | 64 | 128 | 256 | 512 | 1024 | 2048 | 4096 |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_no_opt | 0  | 0   | 0   | 1   | 0    | 0    | 0    |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_opt    | 0  | 0   | 0   | 0   | 0    | 0    | 1    |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_opt_n  | 0  | 0   | 0   | 0   | 0    | 1    | 0    |
+--------------------+----+-----+-----+-----+------+------+------+
| insert_sort        | 0  | 1   | 0   | 0   | 0    | 0    | 1    |
+--------------------+----+-----+-----+-----+------+------+------+
| merge_sort         | 0  | 1   | 1   | 2   | 4    | 9    | 19   |
+--------------------+----+-----+-----+-----+------+------+------+
| sorted             | 0  | 0   | 0   | 0   | 0    | 0    | 1    |
+--------------------+----+-----+-----+-----+------+------+------+
Current data: AC
+--------------------+----+-----+-----+-----+------+------+------+
| Functions/size     | 64 | 128 | 256 | 512 | 1024 | 2048 | 4096 |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_no_opt | 0  | 2   | 10  | 39  | 165  | 662  | 2834 |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_opt    | 0  | 2   | 9   | 31  | 135  | 546  | 2269 |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_opt_n  | 0  | 2   | 7   | 33  | 136  | 597  | 2261 |
+--------------------+----+-----+-----+-----+------+------+------+
| insert_sort        | 0  | 1   | 4   | 16  | 70   | 289  | 1190 |
+--------------------+----+-----+-----+-----+------+------+------+
| merge_sort         | 1  | 0   | 1   | 2   | 5    | 11   | 24   |
+--------------------+----+-----+-----+-----+------+------+------+
| sorted             | 0  | 0   | 0   | 1   | 1    | 1    | 1    |
+--------------------+----+-----+-----+-----+------+------+------+
Current data: WC
+--------------------+----+-----+-----+-----+------+------+------+
| Functions/size     | 64 | 128 | 256 | 512 | 1024 | 2048 | 4096 |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_no_opt | 0  | 4   | 11  | 53  | 203  | 866  | 3483 |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_opt    | 0  | 2   | 10  | 43  | 175  | 716  | 2880 |
+--------------------+----+-----+-----+-----+------+------+------+
| bubble_sort_opt_n  | 1  | 3   | 9   | 43  | 175  | 712  | 2979 |
+--------------------+----+-----+-----+-----+------+------+------+
| insert_sort        | 1  | 1   | 8   | 34  | 141  | 574  | 2351 |
+--------------------+----+-----+-----+-----+------+------+------+
| merge_sort         | 0  | 0   | 1   | 2   | 5    | 9    | 20   |
+--------------------+----+-----+-----+-----+------+------+------+
| sorted             | 0  | 0   | 0   | 0   | 0    | 0    | 0    |
+--------------------+----+-----+-----+-----+------+------+------+
'''
