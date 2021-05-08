array = [1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]

max_count = 0
count = 1
for i in range(len(array) - 1):
    if array[i] % 2 == 1:
        if array[i] == array[i+1]:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count

print(max_count)