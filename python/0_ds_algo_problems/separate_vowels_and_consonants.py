def string_transform(string):
    vowels = ""
    consonants = ""

    all_vowels = ["a", "e", "i", "o", "u"]
    for ele in string:
        if ele in all_vowels:
            vowels += ele
        else:
            consonants += ele
    
    print(vowels + consonants)

tc = int(input())

for i in range(tc):
    n = int(input())
    string = input().strip()
    string_transform(string)

