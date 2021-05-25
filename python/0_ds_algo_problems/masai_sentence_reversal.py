def reverse_sentence(array, start, end):
    i = start
    j = end
    while(i <= j):
        temp = array[i]
        array[i] = array[j]
        array [j] = temp
        i += 1
        j -= 1
    
    return array

def reverse_word(array):
    start_index = 0
    for i in range(len(array)):
        if array[i] == " ":
            reverse_sentence(array, start_index, i-1)
            start_index = i+1
    print(*array)    




array = list(input())
reversed = reverse_sentence(array, 0, len(array) - 1)
reverse_word = reverse_word(reversed)