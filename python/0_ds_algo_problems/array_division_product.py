n = int(input())
array = list(map(int, input().strip().split()))

pairs_product = 1
for i in range(0, n, +2):
    if i + 1 < n:
        pair_sum = array[i] + array[i+1]
        pairs_product *= pair_sum

print(pairs_product)