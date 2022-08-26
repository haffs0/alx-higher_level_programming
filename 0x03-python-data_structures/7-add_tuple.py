#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    
    a = 0; b = 0; c = 0; d = 0;
    if len(tuple_a) < 2 and len(tuple_a) != 0:
        (a, ) = tuple_a
    elif len(tuple_a) != 0:
        (a, b) = tuple_a

    if len(tuple_b) < 2 and len(tuple_b) != 0:
        (c, ) = tuple_b
    elif len(tuple_b) != 0:
        (c, d) = tuple_b

    return (a + c, b + d)
