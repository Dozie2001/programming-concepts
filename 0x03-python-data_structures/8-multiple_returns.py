#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        variable = None
    else:
        variable = (len(sentence), sentence[0])
    return variable
