n = int(input())
array = list(map(int, input().strip().split()))

product = 1
for ele in array:
    product *= ele

print(product)