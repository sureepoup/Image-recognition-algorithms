def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


contour1 = [0+2j, 3+2j, 3+0j, 3-2j, 0-2j, -3-2j, -3-0j, -3+2j]

for i in range(4):
    shift(contour1, -1)
    print(contour1)


