#!usr/bin/python3
def weight_average(my_list=[]):

    score = 0
    weight = 0

    if len(my_list) == 0 or my_list is None:
        return 0

    for tup in my_list:
        score += (tup[0] * tup[1])
        weight += tup[1]
    return score / weight
