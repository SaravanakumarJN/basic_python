def find_index_of_2(array):
    index = -1
    for i in range(len(array) -1):
        if array[i] == 2:
            index = i
    return index

n = int(input())
array = list(map(int, input().strip().split()))

index_of_2 = find_index_of_2(array)
if(index_of_2 == -1):
    print(-1)
else:
    print(array[index_of_2 + 1])
