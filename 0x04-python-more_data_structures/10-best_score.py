#!/usr/bin/python3
def best_score(a_dictionary):
    key = None
    value = None
    b = 0

    if a_dictionary is None:
        return None

    dict_items = [(key, value) for key, value in a_dictionary.items()]

    for i in range((len(dict_items) // 2) + 1):
        k, v = dict_items[i]
        k1, v2 = dict_items[i + 1]

        if v > v2:
            b = v
            key = k
        else:
            if v2 > b:
                b = v2
                key = k1
    return key
