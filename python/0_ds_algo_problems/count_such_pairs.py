n, k = map(int, input().strip().split(" "))
array = list(map(int, input().strip().split(" ")))

such_pair_count = 0
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if(array[i] + array[j] == k):
            such_pair_count += 1

print(such_pair_count)