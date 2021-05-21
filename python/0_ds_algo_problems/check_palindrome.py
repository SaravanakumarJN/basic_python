input = "malayala"

flag = True
i = 0
j = len(input) - 1

for i in range(0, i <= j, 1):
    if input[i] != input[j]:
        flag = False
        print("No")
        break
    j = j - 1

if flag:
    print("Yes")



