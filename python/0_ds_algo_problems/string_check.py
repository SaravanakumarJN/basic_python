def string_type_check(string):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    char_flag = 0
    num_flag = 0

    for ele in string:
        if char_flag == 0 or num_flag == 0:
            if ele in numbers:
                num_flag += 1
            else:
                char_flag += 1
        else:
            return "alphanumeric"

    if num_flag:
        return "numbers"
    else:
        return "chars"

tc = int(input())
for i in range(tc):
    n = int(input())
    string = input()
    print(string_type_check(string))