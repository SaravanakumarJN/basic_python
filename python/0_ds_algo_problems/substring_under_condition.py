string = input().strip()

subs_start_and_end = 0
for i in range(len(string)):
    sub = ""
    for j in range(i, len(string)):
        sub += string[j]
        # print(sub)
        if(sub[0] == sub[len(sub) - 1]):
            subs_start_and_end += 1

print(subs_start_and_end)