string = input()

reversed = ""
for i in range(len(string) - 1, -1, -1):
    reversed += string[i]

print(reversed)