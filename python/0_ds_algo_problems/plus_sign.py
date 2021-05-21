import math

number = int(input())

limit = (number * 2) + 1
for i in range(limit):
    mid = math.floor(limit / 2)
    string = ""
    for j in range(limit):
        if i == mid:
            string += "*"
        else:
            if j == mid:
                string += "*"
            elif j < mid:
                string += " "
    print(string)


