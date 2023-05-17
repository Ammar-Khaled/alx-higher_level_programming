#!/usr/bin/python3
def weight_average(my_list=[]):
    ''''
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    '''
    if not my_list:
        return 0
    weighted_score_sum = 0.0
    weight_sum = 0.0
    for tuple in my_list:
        weighted_score_sum += tuple[0] * tuple[1]
        weight_sum += tuple[1]
    return weighted_score_sum / weight_sum
