array = [1, 3, 2, 4, 2, 1, 6, 5]

distinct = list(set(array))

if len(distinct) < 3:
    print("Not Possible")
    print("Not Possible")

else:
    for i in range(len(distinct)):
        for j in range(i+1,len(distinct)):
            if distinct[i] > distinct[j]:
                swap = distinct[i]
                distinct[i] = distinct[j]
                distinct[j] = swap

    print(*distinct[0:3])
    print(*distinct[-3:])

