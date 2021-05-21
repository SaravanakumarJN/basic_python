def is_prime(num):
    prime = True
    if num < 2 and num >= 0:
        return False

    for i in range(2, num):
        if num % i == 0:
            prime = False
    
    if prime:
        return True
    else:
        return False


prime_or_not = is_prime(5)
print(prime_or_not)

