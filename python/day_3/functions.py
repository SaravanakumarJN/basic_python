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


# 





