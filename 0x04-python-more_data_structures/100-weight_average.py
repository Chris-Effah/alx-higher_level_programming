#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_scores = 0
    sum_weight = 0

    for tuple in my_list:
        sum_scores += tuple[0] * tuple[1]
        sum_weight += tuple[1]

        w_avg = sum_scores / sum_weight
        return w_avg
