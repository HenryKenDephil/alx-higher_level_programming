#!/usr/bin/bash/python3
'''Write a program that prints all numbers
from 0 to 98 in decimal and in hexadecimal'''
for num in range(0, 99):
    print("{0:d} = 0x{0:x}" .format(num))
