# Взаимокорреляционная функция


import numpy


def cross_correlation_function(list1, list2):
    result = 0
    cross_corr_vect = []
    # if (len(list1) != len(list2)) or listsum(list1) != 0 or listsum(list2) != 0:
    #     return print("Error")
    # else:
    steps = 1
    for j in range(len(list2)):
        for i in range(len(list1)):
                result += numpy.vdot(list1[i], list2[i])
        list2 = list2[steps:] + list2[:steps]
        steps += 1
    return print("Scalar product =", result)


def listsum(a):
    sum_list = 0
    for i in a:
        sum_list += i
    return sum_list


contour1 = [0+2j, 3+2j, 3+0j, 3-2j, 0-2j, -3-2j, -3-0j, -3+2j]
contour2 = [0+1j, 1+1j, 1+0j, 1-1j, 0-1j, -1-1j, -1-0j, -1+1j]

