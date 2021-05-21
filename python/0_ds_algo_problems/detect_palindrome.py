def is_palindrome(string):
    reversed = ""
    for i in range(len(string) -1, -1, -1):
        reversed += string[i]
    
    if string == reversed:
        print("Yes")
    else:
        print("No")

def is_palindrome(string):
    i = 0
    j = len(string)
    is_pal = True
    while(i <= j):
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            is_pal = False
            break

    if is_pal:
        print("Yes")
    else:
        print("No")


string = input()

is_palindrome(string)