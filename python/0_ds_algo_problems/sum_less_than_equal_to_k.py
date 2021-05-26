n, k = map(int, input().strip().split(" "))
array = list(map(int, input().strip().split(" ")))

sum = 0
for ele in array:
    if ele <= k:
        sum += ele

print(sum)