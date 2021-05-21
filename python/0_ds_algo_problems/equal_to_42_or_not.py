n = int(input())
array = list(input().strip().split())

flag = False
for ele in array:
    if ele == "42":
        flag = True
        print("Yes")
        break

if not flag:
    print("No")

# if "42" in array:
#     print("Yes")
# else:
#     print("No")