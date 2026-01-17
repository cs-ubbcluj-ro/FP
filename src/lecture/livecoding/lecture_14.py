"""
What an exam day at FP is like :)

    Let's say we start at 09:00 at FSEGA

    09:00 - 10:30 - written test (subject is printed, test is pen and paper)
    10:30 - 11:30 - break
    11:30 - 14:00 - practical test (using your own laptop to write a program)
                  - we grade the written test
    14:00+        - grade the practical test
    14:00+        - discussion for final grade (checking the written paper)
    15:00 - 16:00 - we are done and can go home :)

Recap - algorithm complexity
    BC(A) - input data is organized so that the algorithm makes the minimal number of steps
            ex:
                bubble sort - sort an array that is already sorted
                Important! Array size does NOT matter!

    AC(A) - ?

    WC(A) - input data is organized so that the algorithm makes the maximum number of steps
            ex:
                bubble sort - sort an array that is sorted but in reverse order
                Important! Array size does NOT matter!

    Important - some algorithm don't have distinct best/worst cases

    Example complexity_2 from Exam Guide
        BC(complexity_2) is Theta(1), when the last item in the list is 7
        WC(complexity_2) is Theta(n), when the list does not contain element 7

    def complexity_3(n : int, i : int)
        Time complexity:
            if n = 1 => T(n) = 1 # T(n) is the number of operations made by the algorithm

            if n > 1 => T(n) = 4 * T(n/2) + 1 # we unwind this expression and figure out how to get
            # to T(n), which we know is 1

        Extra-space complexity:
            T(n) = T(n/2) + 1 # we call the function for half the input + the current stack frame
            => Theta(log(n)) extra-space



Example problems
    - Calculate the r-th root of a given number x with a given precision p
    - Given an array of integers, calculate the longest decreasing subsequence of primes contained in it
    - A stair can be climbed by going up 1, 2 or 3 steps at once. Determine in how many ways we can go up a staircase
        of "n" stairs
"""
