array = [1, 2, 3, 4, 5]

# method 1
sum1 = 0
for i in array:
    sum1 += i

print(sum1)

# method 2
sum2 = 0
for i in range(len(array)):
    sum2 += array[i]

print(sum2)