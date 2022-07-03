#!/usr/bin/bash/python3
'''writea function that retrieves an element from from a list like in C'''
'''my_list = [1, 2, 3, 4, 5] will be used to test the function'''


def element_at(my_list, idx):
    items = len(my_list) - 1
    if idx < 0 or idx > items:
        return(None)
    else:
        return my_list[idx]
