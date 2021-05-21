n = int(input())
array = list(map(int, input().strip().split(" ")))

sum = 0
for i in range(len(array)):
    if i % 2 == 0:
        sum += 2 * array[i]
    else:
        sum += 3 * array[i]

print(sum)