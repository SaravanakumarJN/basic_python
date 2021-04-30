input = 20

flag = True
for i in range(2, input):
    if input%i == 0:
        print("No")
        flag = False
        break

if flag:
    print("Yes")