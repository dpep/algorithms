#!/usr/bin/env python

'''
insertion sort

Incrementally move each item into place, adjusting the already sorted
elements as needed.  Useful if list is mostly sorted.

Runtime O(n^2), memory O(1)
'''


def insertion_sort(data):
    for i in range(1, len(data)):
        value = data[i]

        # find proper spot for next element
        j = 0
        while data[j] < value:
            j += 1

        # slide everything down to make room
        for k in range(i, j, -1):
            data[k] = data[k - 1]

        # put item into place
        data[j] = value


def test_it():
    from random import randint

    for i in range(20):
        data = [ randint(-20, 20) for j in range(randint(0, 100)) ]

        insertion_sort(data)
        assert sorted(data) == data
