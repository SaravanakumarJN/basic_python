string = input()

value_map = list("abcdefghijklmnopqrstuvwxyz")

string_value = 0
for ele in string:
    for i in range(len(value_map)):
        if ele == value_map[i]:
            string_value += (i + 1)
            break

print(string_value)