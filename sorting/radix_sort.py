#!/usr/bin/env python

'''
radix sort

Good for sorting integers within a broader range than
might be suitable for a counting sort (eg. n^2).

https://www.geeksforgeeks.org/radix-sort
'''


def counting_sort(data, exp):
    counts = [ 0 ] * 10  # assuming base 10

    # count integer occurrences
    for val in data:
        counts[(val // exp) % 10] += 1

    # translate counts into offsets
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    # create sorted list using counts and offsets
    res = [ None ] * len(data)
    for val in reversed(data):
        i = (val // exp) % 10
        counts[i] -= 1
        res[counts[i]] = val

    # copy results back into place
    for i, val in enumerate(res):
        data[i] = val


def radix_sort(data):
    max_val = max(data)
    exp = 1

    # for each digit, from least significant to most, re-sort list
    while max_val // exp > 0:
        counting_sort(data, exp)
        exp *= 10


def test_it():
    from random import randint

    for i in range(20):
        data = [ randint(0, 1000) for j in range(randint(0, 1000)) ]

        radix_sort(data)
        assert sorted(data) == data
