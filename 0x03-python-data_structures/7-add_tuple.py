#!/usr/bin/bash/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = tuple_a + tuple_b
    tuple_a = (a, b)
    tuple_b = (a1, b2)
    length = len(new_tuple)

    if new_tuple == (tuple_a + tuple_b):
        while length < 2:
            if len(tuple_a) < 2:
                return(a, b)
            elif len(tuple_b) < 2:
                return(a1, b2)
        while length > 2:
            if len(tuple_a) > 2:
                return (a, b)
            elif len(tuple_b) > 2:
                return (a1, b1)
    print("{:d}  {:d}" .format((tuple_a, tuple_b), tuple_a + tuple_b))
