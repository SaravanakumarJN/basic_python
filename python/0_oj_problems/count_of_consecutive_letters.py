string = "aaabbbbccaaddddd"

# while loop
answer = ""
i = 0
while i < len(string):
    count = 0
    for j in range(i, len(string)):
        if string[i] == string[j]:
            count += 1
        else:
            break
    answer += string[i]
    answer += str(count)
    i = i + count

print(answer)

# for loops
answer = ""
i = 0
for i in range(len(string)):
    count = 0

    for j in range(i, len(string)):
        if string[i] == string[j]:
            count += 1
        else:
            break

    answer += string[i]
    answer += str(count)
    # print(i, "before")
    # i = i + count -1
    # print(i)

print(answer)