#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    product_sum = 0
    weight_sum = 0

    for score, weight in my_list:
        product_sum += (score * weight)
        weight_sum += weight

    if weight_sum == 0:
        return 0.0

    return product_sum / weight_sum
