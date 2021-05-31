import math

def is_prime(num):
    if(num == 1 or num == 0):
        return False
    else:
        assume = True
        for i in range(2, num):
            if(num % i == 0):
                assume = False
                break
        
        return assume


n = int(input())
array = list(map(int, input().strip().split(" ")))

sum = 0
for i in range(len(array)):
    for j in range(i+1, len(array)):
        index_diff = j - i
        if is_prime(index_diff):
            sum += abs(array[i] - array[j])

print(sum)
