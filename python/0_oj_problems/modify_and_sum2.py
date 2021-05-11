n = int(input())
array = list(map(int, input().strip().split(" ")))

sum = 0
for i in range(len(array)):
    if i % 2 == 0:
        sum += array[i] + 5
    else:
        sum += array[i] + 7

print(sum)