number = 5

for i in range(number):
    string = ""
    for j in range(number):
        if j < number - i:
            string += " "
        else:
            string += "* "
    print(string)

