#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest_value = 0
    biggest_key = None

    for k, v in a_dictionary.items():
        if v > biggest_value:
            biggest_value = v
            biggest_key = k
    return biggest_key
