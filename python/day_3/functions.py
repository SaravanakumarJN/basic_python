# functions
def add_num(x, y):
    return x + y

print(add_num(10, 20))


# local variable don't affect global
name = "henna"

def function():
    name = "ana"

function()
print(name)


# declare variable inside a function but globally 
name = "henna"

def function():
    global name
    name = "anna"

function()
print(name)


# multiple arguments in functions
def function(*args):
    for i in args:
        print(i)

    for i in range(len(args)):
        print(args[i])

function(1, 2, 3, 4, 5)








