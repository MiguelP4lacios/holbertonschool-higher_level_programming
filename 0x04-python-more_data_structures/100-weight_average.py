#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    weight = 0
    score_weight = 0
    for i in range(len(my_list)):
        a_tuple = my_list[i]
        weight += a_tuple[1]
        score_weight += a_tuple[0] * a_tuple[1]
    return float(score_weight / weight)
