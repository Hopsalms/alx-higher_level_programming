#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    sum_total = 0
    div = 0
    for items in my_list:
        sum_total = sum_total + (items[0] * items[1])
        div = div + items[-1]
    return sum_total/div
