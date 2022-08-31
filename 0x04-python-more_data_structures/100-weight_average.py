#!usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    if not my_list:
        return 0
    for s, w in my_list:
        score += s * w
        weight += w
    return score / weight
