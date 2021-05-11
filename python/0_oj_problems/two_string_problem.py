str1 = input()
str2 = input()

# if str2 in str1:
#     print("Yes")
# else:
#     print("No")

flag = False
i = 0
while i < len(str1):
    if str1[i] == str2[0] and (( i + len(str2) -1 ) < len(str1)):
        j = 1
        k = i + 1
        while j < len(str2):
            if str1[k] != str2[j]:
                break
            j += 1
            k += 1
        if j == len(str2):
            flag = True
            break
    i += 1

if flag:
    print("Yes")
else:
    print("No")



