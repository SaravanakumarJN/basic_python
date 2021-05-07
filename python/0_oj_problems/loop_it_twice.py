L, R = list(map(int, input().split()))

result = ""
for i in range(L, R+1, 2):
    result = result + str(i) + " "

print(result)