#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    """ This function adds 2 tuples """

    ta_len = len(tuple_a)
    tb_len = len(tuple_b)
    tupl = tuple_a, tuple_b
    if (not ta_len >= 2) or (not tb_len >= 2):
        if (((ta_len < 2) and (tb_len < 2)) and (ta_len != 0 and tb_len != 0)):
            tupl = tuple_a[0] + tuple_b[0], 0
        elif (((ta_len < 2) and (ta_len != 0))) and (tb_len >= 2):
            tupl = (tuple_a[0] + tuple_b[0]), (0 + tuple_b[1])
        elif (ta_len >= 2) and ((tb_len < 2) and (tb_len != 0)):
            tupl = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0)
        elif (ta_len == 0) and ((tb_len < 2) and (tb_len != 0)):
            tupl = 0 + tuple_b[0], 0
        elif ((ta_len < 2) and (ta_len != 0)) and (tb_len == 0):
            tupl = tuple_a[0] + 0, 0
        elif (ta_len >= 2) and (tb_len == 0):
            tupl = tuple_a[0] + 0, tuple_a[1] + 0
        elif (ta_len == 0) and (tb_len >= 2):
            tupl = tuple_b[0] + 0, tuple_b[1] + 0
    else:
        tupl = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])

    return tupl
