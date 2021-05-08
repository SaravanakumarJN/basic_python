n = int(input())
array = list(map(int, input().split()))

odd_sum = 0
even_sum = 0
for ele in array:
    if ele % 2 == 0:
        even_sum += ele
    else:
        odd_sum += ele

if odd_sum > even_sum:
    print("Odd")
else:
    print("Even")