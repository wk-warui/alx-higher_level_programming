#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    diff = list(a_dictionary.keys())[0]
    big = a_dictionary[diff]
    for k, l in a_dictionary.items():
        if l > big:
            big = l
            diff = k
    return (diff)
