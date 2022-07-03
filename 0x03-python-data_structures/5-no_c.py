#!/usr/bin/bash/python3


def no_c(my_string):
    length = len(my-string)

    j = 0

    new_string = my-string[:]

    for i in range(lenth):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new_string = new-string[:(i - j)] + my_string[(i + 1):]
            j += 1

    return(new_string)
