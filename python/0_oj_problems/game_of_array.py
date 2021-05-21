n, k = list(map(int, input().strip().split()))
array = list(input().strip().split())

no_rot = k
if k >= n:
    no_rot = k % n

after_rot = []
i = no_rot
while(i < n):
    after_rot.append(array[i])
    i += 1

i = 0
while(i < no_rot):
    after_rot.append(array[i])
    i += 1

print(*after_rot)