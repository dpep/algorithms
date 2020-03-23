#!/usr/bin/env python

'''
quick sort

For a given list of elements, partition them so that smaller
elements are on the left side and larger elements are on the right.
Recursively apply to each half.
'''


def quick_sort(data):
    def _sort(start, end):
        if start >= end:
            # base case, nothing left to sort
            return

        # pick an arbitrary value to partition around
        partition_val = data[start]
        partition_i = start

        # move each element into its proper partition
        for j in range(start + 1, end + 1):
            if data[j] <= partition_val:
                # swap this smaller value into left partition
                partition_i += 1
                data[partition_i], data[j] = data[j], data[partition_i]

        # swap partitioning value into place, so that all values
        # leftward are less than or equal to and all values
        # rightward are greater than
        data[start], data[partition_i] = data[partition_i], data[start]

        # then recursively partition each partition, excluding
        # the element used to partition
        _sort(start, partition_i - 1)
        _sort(partition_i + 1, end)

    _sort(0, len(data) - 1)


def test_it():
    from random import randint

    for i in range(10):
        data = [ randint(-100, 100) for j in range(randint(0, 10)) ]

        quick_sort(data)
        assert sorted(data) == data
