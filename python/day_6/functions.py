'''
Functions 
=> pass by value        (immutable datatypes)
=> pass by reference    (mutable datatypes)
'''


# passing immutable data type inside function
def func(num):
    num += 5
    print(id(num))
n = 5

## before calling
print(id(n))

func(n)

## after calling
print(id(n))



# passing mutable data type inside function
def func1(array):
    array.append(1)
array = [1, 2, 3, 4]

## before calling
print(array)
print(id(array))

func1(array)

## after calling
print(array)
print(id(array))
