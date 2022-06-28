#!/usr/bin/bash/python3
'''Write a program that prints the ASCII alphabet,
in lowercase, not followed by a new line.
'''
for ch in range(97, 123):
    if ch != 101 and ch != 113:
        print("{:c}" .format(ch), end='')
