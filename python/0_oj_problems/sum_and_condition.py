n = int(input())
array = list(map(int, input().strip().split()))

array_sum = 0
for ele in array:
    array_sum += ele

if array_sum > 100:
    print("Greater")
else:
    print("Lesser")