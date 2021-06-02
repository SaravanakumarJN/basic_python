n = int(input())
array = list(map(int, input().strip().split(" ")))

long = 0
i = 0
while i < len(array):
    if array[i] % 2 == 1:
        count = 1
        j = i + 1
        while j < len(array):
            if array[j] != array[i]:
                if long < count:
                    long = count
                break
            else:
                count += 1
            j += 1
        i = j - 1
        if i == len(array) - 1 and long < count:
            long = count

    i += 1
    
print(long)