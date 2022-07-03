#!/usr/bin/bash/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return(None)
    max_value = max_integer(my_list)
    for i in range(1, length):
        if my_list[i] == max_value:
            return(my_list[i])
        print("max_value is {:d}". format(max_value))
