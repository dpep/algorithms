#!/usr/bin/env python

'''
merge sort

Recursively divide a list of elements in half, then merge them
back together in sorted order.  Runtime O(nlg(n)), memory O(n)
'''


def merge_sort(data):
    if len(data) <= 1:
        # base case, when there is no data to sort
        return data

    # recursively divide data
    mid = len(data) // 2
    one_half = merge_sort(data[:mid])
    other_half = merge_sort(data[mid:])

    # merge the two sorted halves together in order
    res = []
    i = j = 0

    while i < len(one_half) and j < len(other_half):
        if one_half[i] <= other_half[j]:
            res.append(one_half[i])
            i += 1
        else:
            res.append(other_half[j])
            j += 1

    if i < len(one_half):
        res += one_half[i:]
    else:
        res += other_half[j:]

    return res


def test_it():
    from random import randint

    for i in range(10):
        data = [ randint(-100, 100) for j in range(randint(0, 20)) ]

        assert sorted(data) == merge_sort(data)
