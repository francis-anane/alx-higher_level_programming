#!/usr/bin/python3

def multiple_returns(sentence):

    """ This function returns a tuple containing the length of a string
    and it first character.
    """

    slen = len(sentence)
    if slen == 0:
        return (0, None)
    else:
        return (slen, sentence[0])
