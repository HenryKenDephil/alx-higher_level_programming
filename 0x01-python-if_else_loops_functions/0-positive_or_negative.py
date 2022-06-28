#!/usr/bin/bash/python3
'''program will assign a random signed number to the variable
number each time it is executed.
The variable number will store a different value
every time you will run this program'''

import random
number = random.randint(-10, 10)

for i in range(number):
    if i > 0:
        print("{:d} is positive".format(i))
    elif i == 0:
        print("{:d} is zero" .format(i))
    else:
        print("{:d} is negative" .format(i))
