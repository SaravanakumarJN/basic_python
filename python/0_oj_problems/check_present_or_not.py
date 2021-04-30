to_find = 20
array = [20, 30, 10, 4, 5, 15, 30]

# method 1
flag = False
for i in array:
    if i == to_find:
        flag = True
        print("Yes")
        break

if not flag:
    print("No")


# method 2
if to_find in array:
    print("Yes")
else:
    print("No")




