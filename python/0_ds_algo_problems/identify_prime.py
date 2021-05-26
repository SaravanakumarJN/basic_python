def is_prime(number):
    if number == 1 or number == 0:
        return False

    prime = True
    for i in range(2, number -1):
        if number % i == 0:
            prime = False
            break

    return prime

number = int(input())

if is_prime(number):
    print("Yes")
else:
    print("No")