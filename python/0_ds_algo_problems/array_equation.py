n = int(input())
array = list(map(int, input().strip().split(" ")))

odd_sum = 0
even_sum = 0
for ele in array:
    if ele % 2 == 0:
        even_sum += ele
    else:
        odd_sum += ele

x = even_sum
y = odd_sum

print((2 * x) + (3 * y))