n = int(input())
array = list(map(int, input().strip().split()))

pairs_sum = 0
for i in range(0, n, +2):
    if i + 1 < n:
        pair_product = array[i] * array[i+1]
        pairs_sum += pair_product

print(pairs_sum)