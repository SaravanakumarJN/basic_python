tc = int(input())

for i in range(tc):
    n = int(input())
    string = input()

    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num_count = ""
    curr_alphabet = string[0]
    answer = ""

    j = 1
    while(j < len(string)):
        if string[j] in num:
            num_count += string[j]
        else:
            k = 0
            while(k < int(num_count)):
                answer += curr_alphabet
                k += 1
            curr_alphabet = string[j]
            num_count = ""
        j+= 1
    
    k = 0
    while(k < int(num_count)):
        answer += curr_alphabet
        k += 1

    print(answer)
    
