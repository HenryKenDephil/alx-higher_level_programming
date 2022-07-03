#!/usr/bin/bash/python3
def divisible_by_2(my_list=[]):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            print("{:d} is True" .format(my_list))
        else:
            print("{:d} is False" .format(my_list))
