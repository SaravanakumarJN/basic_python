def is_palindrome(string):
    assume = True

    i = 0
    j = len(string) - 1
    while(i <= j):
        if(string[i] != string[j]):
            assume = False
            break
        i += 1
        j -= 1
    
    return assume

string = input().strip()

longest_pal_length = 0
for i in range(len(string)):
    subs = ""
    for j in range(i, len(string)):
        subs += string[j]
        if is_palindrome(subs) and longest_pal_length < len(subs):
            longest_pal_length = len(subs)

print(longest_pal_length)

