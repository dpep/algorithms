#!/usr/bin/env python

'''
selection sort

Continuosly find the smallest value our of order and swap it into place.

Runtime O(n^2), memory O(1)
'''


def selection_sort(data):
    for i in range(len(data) - 1):
        # find smallest value in unordered section of list
        smallest = i
        for j in range(i + 1, len(data)):
            if data[j] < data[smallest]:
                smallest = j

        # swap smallest value into place
        data[i], data[smallest] = data[smallest], data[i]


def test_it():
    from random import randint

    for i in range(20):
        data = [ randint(-20, 20) for j in range(randint(0, 100)) ]

        selection_sort(data)
        assert sorted(data) == data
