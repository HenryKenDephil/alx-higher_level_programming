#!/usr/bin/bash/python3
def multiple_returns(sentence):
    len_sen = len(sentence)

    if (len_sen == 0):
        if sentence == " ":
            return 0, None
        return len(sentence), sentence[0]
