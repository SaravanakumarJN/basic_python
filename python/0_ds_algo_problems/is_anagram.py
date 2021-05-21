def is_anagram(string1, string2):
    char_count_in_string1 = {}
    char_count_in_string2 = {}
    
    for ele in string1:
        if ele != ' ':
            if char_count_in_string1.get(ele) == None:
                char_count_in_string1[ele] = 1
            else:
                char_count_in_string1[ele] += 1

    for ele in string2:
        if ele != " ":
            if char_count_in_string2.get(ele) == None:
                char_count_in_string2[ele] = 1
            else:
                char_count_in_string2[ele] += 1

    is_ana = True
    for key in char_count_in_string1:
        if char_count_in_string1[key] == char_count_in_string2[key]:
            continue
        else:
            is_ana = False
            break

    if is_ana:
        print("True")
    else:
        print("False")


string1 = input().strip()
string2 = input().strip()

is_anagram(string1, string2)