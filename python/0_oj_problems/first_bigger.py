def find_closest_greater(array, num):
    closest_greater = float("inf")
    for ele in array:
        if ele > num and closest_greater > ele:
            closest_greater = ele
    if(closest_greater == float('inf')):
        return -1
    else:
        return closest_greater

n = int(input())
array = list(map(int, input().strip().split()))
tc = int(input())

for i in range(tc):
    num = int(input())
    print(find_closest_greater(array, num))