#!/usr/bin/env python

'''
bubble sort

Where all sorting journies begin.  Repeatedly swap neighboring values
into their correct order until the entire array is sorted.

Runtime O(n^2), memory O(1)
'''


def bubble_sort(data):
    made_swap = True
    while made_swap:
        made_swap = False
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    # swap values
                    data[i], data[j] = data[j], data[i]
                    made_swap = True


def test_it():
    from random import randint

    for i in range(20):
        data = [ randint(-20, 20) for j in range(randint(0, 100)) ]

        bubble_sort(data)
        assert sorted(data) == data
