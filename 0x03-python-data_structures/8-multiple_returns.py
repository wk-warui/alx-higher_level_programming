#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_s = ()
    if len(sentence) == 0:
        tuple_s = 0, "None"
    else:
        tuple_s = len(sentence), sentence[0]
    return tuple_s
