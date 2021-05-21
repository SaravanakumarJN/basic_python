number = int(input())

for i in range(1, number+1):
    string = ""
    for j in range(1, i+1):
        string += str(j) + " "
    print(string.strip())

    