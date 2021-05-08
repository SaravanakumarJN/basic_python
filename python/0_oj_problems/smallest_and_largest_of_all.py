n = int(input())
array = list(map(int, input().strip().split()))

max = array[0]
min = array[0]
for ele in array:
    if(max < ele):
        max = ele
    if(min > ele):
        min = ele

print(min)
print(max)