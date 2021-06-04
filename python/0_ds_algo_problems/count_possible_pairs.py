n, m = map(int, input().strip().split(" "))

count = 0
till = max(m, n)
for i in range(0, till + 1):
  for j in range(0, till + 1):
    if((i**2) + j == n) and ((j**2) + i == m):
      count += 1

print(count)