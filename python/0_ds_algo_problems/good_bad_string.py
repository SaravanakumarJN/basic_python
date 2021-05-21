def to_good(string):
    good_string = []
    for i in range(len(string)):
        if len(good_string) == 0 or good_string[len(good_string) - 1] != string[i]:
            good_string.append(string[i])
    separator = ""
    print(separator.join(good_string))

tc = int(input())

for i in range(tc):
    string = input()
    to_good(string)