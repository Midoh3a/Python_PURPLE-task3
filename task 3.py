def square(list, x, y):
    for i in list[x:y]:
        for z in range(x, y):
            if i / z == z:
                print(i)


square([1, 2, 4, 5, 6, 7, 64, 8, 9, 2, 16, 25, 15, 36, 12, 49, 15], 1, 200)
