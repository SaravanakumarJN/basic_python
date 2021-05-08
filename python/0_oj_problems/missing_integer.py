array = list(map(int, input().strip().split()))

for i in range(1, (len(array) + 2)):
    flag = False
    for ele in array:
        if i == ele:
            flag = True
            break
    if flag:
        continue
    else:
        print(i)
        break

