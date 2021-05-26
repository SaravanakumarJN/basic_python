def check_loop(array):
    only_distinct = set(array)
    
    if len(only_distinct) == len(array):
        return False
    else:
        return True

tc = int(input())

for i in range(tc):
    n = int(input())
    array = list(map(int, input().strip().split()))

    if check_loop(array):
        print("Loop")
    else:
        print("Not Loop")
