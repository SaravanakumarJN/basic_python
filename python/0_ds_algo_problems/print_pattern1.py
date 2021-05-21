input = input()

input = int(input)

for i in range (input):
    string = ""
    for j in range (1, 2 * input, 1):
        if j >= input - i and j <= input + i:
            string += "*"
        else:
            string += " "
    print(string)
    