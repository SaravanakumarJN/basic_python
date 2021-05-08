n = int(input())
array = list(map(int, input().strip().split()))

negativity_count = 0
for ele in array:
    if ele < 0:
        negativity += 1

print(negativity)