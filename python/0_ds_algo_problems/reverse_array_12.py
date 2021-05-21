n = int(input())
array = list(input().strip().split())

string = ""
for i in range(len(array) - 1, -1, -1):
    string += array[i] + " "

print(string.strip())