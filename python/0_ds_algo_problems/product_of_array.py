import math

def product_of_array(array):
    product = 1
    for i in array:
        product = product * i
    return product

def prod_except_curr_ele(array, prod_of_array):
    string = ""
    for i in array:
        string += str(math.floor(prod_of_array/i)) + " "
    print(string.strip())

tc = int(input())

for i in range(1, tc + 1):
    n = int(input())
    array = list(map(int, input().strip().split()))

    total = product_of_array(array)
    prod_except_curr_ele(array, total)
