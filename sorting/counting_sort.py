#!/usr/bin/env python

'''
counting sort

Great for sorting integers within a known range of k, especially
when there are lots of duplicates.

Runtime O(n + k), memory O(k)
'''


def counting_sort(data):
    counts = [ 0 ] * (max(data) + 1)

    # count integer occurrences
    for val in data:
        counts[val] += 1

    # rewrite list in sorted order
    i = 0
    for val, count in enumerate(counts):
        for j in range(count):
            data[i] = val
            i += 1


def counting_more_sort(data):
    '''
    handle negative numbers and be more space efficient by
    normalizing values
    '''
    floor = min(data)
    counts = [ 0 ] * (max(data) - floor + 1)

    # count integer occurrences
    for val in data:
        counts[val - floor] += 1

    # rewrite list in sorted order
    i = 0
    for val, count in enumerate(counts):
        for j in range(count):
            data[i] = val + floor
            i += 1


def test_it():
    from random import randint

    for i in range(10):
        data = [ randint(0, 10) for j in range(randint(0, 100)) ]

        counting_sort(data)
        assert sorted(data) == data


def test_more():
    from random import randint

    for i in range(10):
        data = [ randint(-10, 10) for j in range(randint(0, 100)) ]

        counting_more_sort(data)
        assert sorted(data) == data
