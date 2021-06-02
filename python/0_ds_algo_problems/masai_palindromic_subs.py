def is_palindrome(str):
    i = 0
    j = len(str) - 1
    while(i <= j):
        if(str[i] != str[j]):
            return False
        i += 1
        j -= 1
    return True

string = input().strip()

long_palindrome = 0
for i in range(len(string)):
    subs = ""
    for j in range(i, len(string)):   
        subs += string[j]
        if is_palindrome(subs) and long_palindrome < len(subs):
            long_palindrome = len(subs)

print(long_palindrome)