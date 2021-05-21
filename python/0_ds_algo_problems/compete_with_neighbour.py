array = [1, 2, 3, 4, 2, 1, 6, 5]

count = 0
for i in range(len(array)):
    if i == 0:
        if array[i] > array[i+1]:
            count += 1
    elif i == len(array) -1:
        if array[i] > array[i-1]:
            count += 1
    else:
        if array[i] > array[i+1] and array[i] > array[i-1]:
            count += 1

print(count)
    