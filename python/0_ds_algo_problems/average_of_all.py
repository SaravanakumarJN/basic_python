import math

n = int(input())
array = list(map(int, input().strip().split()))

sum = 0
for i in array:
    sum += i

average = math.ceil(sum / n)
print(average)
