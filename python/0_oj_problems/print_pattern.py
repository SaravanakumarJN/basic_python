number = input()

number = int(number)
for i in range(number):
    string = ""
    for j in range(number):
        if j >= number - 1 - i:
            string += "*" 
        else:
            string += " "
    print(string)




