#!/usr/bin/python3

def max_integer(my_list=[]):
    a = 0
    c = 0
    if len(my_list) == 0:
        return (None)

    while a != len(my_list) - 1:
        if my_list[a] > my_list[a + 1]:
            if my_list[a] > c:
                c = my_list[a]
        else:
            if my_list[a + 1] > c:
                c = my_list[a + 1]
        a += 1
    return (c)
