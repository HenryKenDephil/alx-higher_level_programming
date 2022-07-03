#!/usr/bin/bash/python3
'''write a function that replaces an element of a list'''


def replace_in_list(my_list, idx, element):
    for idx in range(len(my_list)):
        if idx < 0 or idx > len(my_list) - 1:
            return (my_list)
        new_list = replace_in_list(my_list, idx, new_element)
        if my_list[idx] == element:
            new_element = my_list[idx]
        else:
            print(new_list)
