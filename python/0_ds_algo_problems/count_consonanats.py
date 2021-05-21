string = input()

count = 0
for ele in string:
    if ele == "a" or ele == "e" or ele == "i" or ele == "o" or ele == "u":
        continue
    else:
        count += 1

print(count)