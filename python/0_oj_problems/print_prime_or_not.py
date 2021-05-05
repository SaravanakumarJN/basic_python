array = [10, 2, 3, 5, 7 ,20, 21, 31]

def check_prime(number):
    if number == 0 or number == 1:
        return False
    
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        return True
    else:
        return False
        
for i in array:
    if check_prime(i):
        print("Prime")
    else:
        print("Not Prime")


