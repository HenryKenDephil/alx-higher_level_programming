#!/usr/bin/bash/python3
'''Write a program that prints all possible
different combinations of two digits'''

for num in range(0, 90):
    if num % 10 >= 0:
        if num != 90:
            print("{:02d}, " .format(num), end='')
        for num in range(0, 10):
            if num >= 10:
                print("{:02d}, " .format(num))
    else:
        print("{:02d}" .format(num))
