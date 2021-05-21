number = int(input())


for i in range(number):
    string = ""
    for j in range(number):
        if i == 0 or i == number - 1 or j == number - 1:
            string += "* "
        else:
            string += "  "
    print(string)
