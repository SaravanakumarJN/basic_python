#decorators (wrapping a functionality around a function)

## without arguments function  [Note : doesn't work for function with argument]
def decorator(function):
    def inner():
        print("Start")
        function()
        print('End')

    return inner

### 1
def hello_world():
    print("Hello World")

hello_world_call = decorator(hello_world)
hello_world_call()

### 2
@decorator
def hello_user():
    print("Hello User")

hello_user()



## with arguments or without argument function  [Note : doesn't work for keyword argument]
def decorator1(function):
    def inner(*args):
        print("Start")
        function(*args)
        print("End")

    return inner

@decorator1
def hello():
    print("Hello")

@decorator1
def user(user):
    print(user)

hello()
user("Saravana")



## with arguments or without argument function including keyword argument
def decorator2(function):
    def inner(*args1, **args2):
        print("Start")
        function(*args1, **args2)
        print("End")

    return inner

@decorator2
def Hi():
    print("Hi")

@decorator2
def username(user):
    print(user)

@decorator2
def user_city(city = "N/A"):
    print(city)

Hi()
username("Saravana")
user_city(city = "Chennai")

