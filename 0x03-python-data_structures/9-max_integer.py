#!/usr/bin/python3


def max_integer(my_list=[]):
    count = len(my_list)
    if count == 0:
        return None
    biggest = my_list[0]
    for i in range(0,len(my_list)):
        if my_list[i] > biggest:
            biggest = my_list[i]
    return biggest
