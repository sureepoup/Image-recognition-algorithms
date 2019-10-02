def equalise(cont1, cont2):
    l = min(len(cont1), len(cont2))
    newcont1 = [0] * l
    newcont2 = [0] * l
    for i in range(l):
        newcont1[i] = cont1[i*len(cont1)//l]
        newcont2[i] = cont2[i*len(cont2)//l]
    return newcont1, newcont2


contour1 = [0+2j, 3+2j, 3+0j, 3-2j, 0-2j, -3-2j, -3-0j, -3+2j]
test1 = [1+1j, 1-1j, -1-1j, -1+1j]
print(equalise(contour1, test1))
