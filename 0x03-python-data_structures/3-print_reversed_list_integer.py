#!/usr/bin/bash/python3
'''write a function that prints all integers\
     of a list, reverse order'''


def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        print("{:d}" .format(i))
