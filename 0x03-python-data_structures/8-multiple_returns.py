#!/usr/bin/python3

def multiple_returns(sentence):

    first_char = None
    sent_len = 0

    if sentence != "":
        first_char = sentence[0]
        sent_len = len(sentence)

    return (sent_len, first_char)
