# some common methods

# uppercase conversion
string = "saravana"
print(string.upper())


# lowercase conversion
string = "SARAvana"
print(string.lower())


# split strings
string = "python for backend"
string_array = string.split(" ")
print(string_array)


# empty separator (split)
string = "python for backend"
string_array = list(string)
print(string_array)


# map (similar to js)
array = [1, 2, 3, 4, 5]

## multiply by 2
def mult_2(number):
    return 2 * number

answer = list(map(mult_2 , array))
print(answer)

## convert array ele to numbers
array = ["1", "2", "3", "4", "5"]

array = list(map(int, array))
print(array)


# set (removes duplicate)
array = [1, 2, 3, 4, 1, 2]
print(set(array))




