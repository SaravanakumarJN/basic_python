array = [13, 4, 5, 67, 8, 1, 29, 4]

def check_prime(number):
    if number == 1 or number == 0:
        return False
    
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    return is_prime

answer = 0
for i in range(len(array)):
    for j in range(i+1, len(array)):
        diff = j - i
        # print(diff)
        if check_prime(diff):
            # print(diff, "pri")
            answer += abs(array[i] - array[j])
    
print(answer)

