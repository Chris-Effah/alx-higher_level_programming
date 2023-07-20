#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_scores = 0
    sum_weight = 0

    for score, weight in my_list:
        sum_scores += score * weight
        sum_weight += weight

    w_avg = sum_scores / sum_weight
    return w_avg
