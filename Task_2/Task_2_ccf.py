import numpy as np

def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

def scalar(cont1,cont2):
    return sum([np.vdot(a,b) for (a,b) in zip(cont1,cont2)])

def vkf(cont1,cont2):
    return [scalar(a, cont2) for a in [cont1[i:]+cont1[0:i+1] for i in range(len(cont1))]]

def scalar_product(list1, list2):
    result = 0

    for i in range(len(list1)):
            result += np.vdot(list1[i], list2[i])
    return result


def cross_correlation_function(list1, list2):
    result = []
    arr = list2
    for i in range(len(arr)):
        result.append(scalar_product(list1, arr))
        shift(arr, 1)
    return result

def auto_corr_func(lst):
    akf = cross_correlation_function(lst, lst)
    return akf

def wawelet(lst):
    arr = []
    arr.append(sum(auto_corr_func(lst)))
    arr.append(sum(auto_corr_func[:len(lst) // 2] + [i * (-1) for i in auto_corr_func[len(lst) // 2:]]))
    arr.append(sum(auto_corr_func[:len(lst) // 3] + [i * (-1) for i in auto_corr_func[len(lst) // 3:2 * (len(lst) // 3)]] + akf[2 * (
                len(lst) // 3):]))
    return arr

def wawelet1(cont1):
    arr = []
    akf = vkf(cont1, cont1)
    arr.append(sum(akf))
    arr.append(sum(akf[:len(cont1) // 2] + [i * (-1) for i in akf[len(cont1) // 2:]]))
    arr.append(sum(akf[:len(cont1) // 3] + [i * (-1) for i in akf[len(cont1) // 3:2 * (len(cont1) // 3)]] + akf[2 * (
                len(cont1) // 3):]))
    return arr




contour1 = [0+2j, 3+2j, 3+0j, 3-2j, 0-2j, -3-2j, -3-0j, -3+2j]
contour2 = [0+1j, 1+1j, 1+0j, 1-1j, 0-1j, -1-1j, -1-0j, -1+1j]
test1 = [1+1j, 1-1j, -1-1j, -1+1j]
test2 = [1+1j, 1-1j, -1-1j, -1+1j]
print(cross_correlation_function(contour1, contour2))
print(cross_correlation_function(test1, test2))
print(wawelet1(test1))
