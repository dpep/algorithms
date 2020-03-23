#!/usr/bin/env python

# Write a function that produces the nth value in the
# fibonacci sequence. Optimal solutions have runtime of O(n) and
# memory O(1).
# https://en.wikipedia.org/wiki/Fibonacci_number
SEQUENCE = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]

__all__ = [
    'fib_recursive',
    'fib_iterative',
    'fib_memoized',
    'fib_round_robin',
]


def fib_recursive(n):
    '''
    Recursive solution.  Eloquent and consice, yet impractical for
    large values of n since it's runtime is O(2^n).
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    '''
    Iterative version with runtime O(n) and memory O(1)
    '''
    if n == 0:
        return 0

    prev = 0
    cur = 1
    for i in range(2, n + 1):
        prev, cur = cur, prev + cur

    return cur


def fib_memoized(n):
    '''
    Iterative approach with runtime of O(n) and memory of O(n).
    Memoized values might be useful if cached for frequent reuse.
    '''
    res = [ 0, 1 ] + [ None ] * n

    for i in range(2, n + 1):
        res[i] = res[i - 1] + res[i - 2]

    return res[n]


def fib_round_robin(n):
    '''
    A slicker version of fib_iterative.  Runtime O(n), memory O(1)
    '''
    res = [ 0, 1, 1 ]
    size = 3

    for i in range(3, n + 1):
        res[i % size] = res[(i - 1) % size] + res[(i - 2) % size]

    return res[n % size]


# test all fibonacci functions
def test_all():
    for fn_name in __all__:
        fib = globals()[fn_name]

        for i in range(len(SEQUENCE)):
            assert SEQUENCE[i] == fib(i)
