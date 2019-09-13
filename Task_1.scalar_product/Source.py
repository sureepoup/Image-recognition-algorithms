def scalar_product(list1, list2):
    result = 0
    if (len(list1) != len(list2)) or listsum(list1) != 0 or listsum(list2) != 0:
        return print("Error")
    else:
        for i in range(len(list1)):
            result += list1[i] * list2[i]
    return print("Scalar product =", result)


def listsum(a):
    sum_list = 0
    for i in a:
        sum_list += i
    return sum_list


contour1 = [0+2j, 3+2j, 3+0j, 3-2j, 0-2j, -3-2j, -3-0j, -3+2j]
contour2 = [0+1j, 1+1j, 1+0j, 1-1j, 0-1j, -1-1j, -1-0j, -1+1j]
scalar_product(contour1, contour2)
