def greater_ahead_count(array):
    i = 1
    count = 0
    while(i < len(array)):
        if array[i-1] > array[i]:
            count += 1
        i += 1
    print(count)
    


tc = int(input())

for i in range(tc):
    n = int(input())
    array = list(map(int, input().strip().split()))

    greater_ahead_count(array)
    