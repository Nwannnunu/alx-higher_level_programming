#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """finds all multiples of 2"""
    multiples = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return multiples
