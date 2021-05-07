L, R = list(map(int, input().strip().split()))

result = ""
i = L
while i <= R:
    result = result + str(i) + " "
    i = i * 2

print(result.strip())