string = input()

i = 0
answer = ""
while i < len(string):
    while i+1 < len(string) and string[i] == string[i+1]:
        i += 2
    if(i < len(string)):
        answer += string[i]
    i += 1

if answer == "":
    print("Empty String")
else:
    print(answer)
    
