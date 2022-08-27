#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)

    for idxs, item in enumerate(my_list):
        if idx == idxs:
            my_list.remove(my_list[idx])
    return (my_list)
