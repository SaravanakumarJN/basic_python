L, R = list(map(int, input().split()))

string = ""
for i in range(L, R+1):
    if i == 0 or i == 1:
        continue
    else:
        flag = True
        for j in range (2, i):
            if i % j == 0:
                flag = False
        if flag:
            string += str(i) + " "

print(string)