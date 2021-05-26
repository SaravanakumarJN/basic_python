def is_odd_count_odd(array):
    count = 0
    for ele in array:
        if ele % 2 != 0:
            count += 1
    if count % 2 != 0:
        return True
    else:
        return False

tc = int(input())

for i in range(tc):
    n = int(input())
    array = list(map(int, input().strip().split(" ")))
    
    if is_odd_count_odd(array):
        print("Yes")
    else:
        print("No")