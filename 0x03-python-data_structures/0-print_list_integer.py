#!/usr/bin/bash/python3
'''write a function that prints all integers of a list'''
'''my_list = [2, 5, 9, 10, 54, 87, 60] can be used to test the function'''


def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}" .format(i))
