#!/usr/bin/python3
def multiple_returns(sentence):
    strLen = len(sentence)
    if strLen == 0:
        firstChr = None
    else:
        firstChr = sentence[0]

    tup = (strLen, firstChr)
    return (tup)
