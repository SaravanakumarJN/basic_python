number = 5

for i in range(number):
    string = ""
    for j in range(number):
        if i < number - 1:
            if j == number - 1:
                string += "* "
            else:
                string += "  "
        else:
            string += "* "
    print(string)

    

