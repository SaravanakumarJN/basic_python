import math

def get_reverse_string(string):
    reversed = ""
    for i in range(len(string) -1, -1, -1):
        reversed += string[i]

    return reversed


string = input()
mid = math.floor(len(string)/2)

result = ""
if len(string) % 2 == 1:
    left = string[0:mid]
    right = string[mid+1:]
    r_left = get_reverse_string(left)
    r_right = get_reverse_string(right)
    result += r_left + string[mid] + r_right

else:
    left = string[0:mid]
    right = string[mid:]
    r_left = get_reverse_string(left)
    r_right = get_reverse_string(right)
    result += r_left + r_right

print(result)



