# Classes  (Structure or blueprint of an object)
'''
=> creating
=> pass
=> variables
=> init
=> functions
=> self
=> del

=> base class
'''


## creating class
class MyClass:
    pass

obj1 = MyClass()
print(type(obj1))



## creating class with class variable
class MyClass1:
    name = "Saravana"
    age = 22

class1_instance = MyClass1()

### 1 class variable
print(class1_instance.name)

### 2 new variable  [not class variable]
class1_instance.gender = "Male"
print(class1_instance.gender)



## creating class with instance variable using init (similar to constructor in JS)
### 1 Without default
class MyClass2:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
class2_instance = MyClass2("Saravana", "22")
print(class2_instance.name)
print(class2_instance.age)

### 2 With default
class MyClass3:
    def __init__ (self, name = "N/A", age = "N/A"):
        self.name = name
        self.age = age
    
class3_instance = MyClass3()
print(class3_instance.name)
print(class3_instance.age)



## creating class and writing class functions or methods
class MyClass4:
    def __init__(self, name = "User", age = 0):
        self.name = name
        self.age = age
    
    # user defined class functions
    def print_info(self):
        print('%s is %d years old' %(self.name, self.age))

class4_instance = MyClass4("Saravana", 22)
class4_instance.print_info()



## delete instance or the attributes that we passed to the instance
del class4_instance
# class4_instance.print_info()          # As class4_instance was deleted, it will throw an error.



## inheriting a class 
'''
=> only the class variable is accessible by child
=> if both the base class and inheriting class has same variable, base class variable is overwitten by inheriting class variable
=> if both the base class and inheriting class has same method, base class method is overwitten by inheriting class method
'''
class Parent():
    father_name = "FFFF"
    mother_name = "MMMM"

    def parent_details(self):
        print("Father : %s" %(self.father_name))
        print("Mother : %s" %(self.mother_name))

class Children(Parent):                 # Parent is inherited to Children class, Now we have access to class variables and methods of Parent class
    name = "CCCC"

    def child_details(self):
        print('%s is the father of %s' %(self.father_name, self.name))

child_instance_1 = Children()
child_instance_1.parent_details()
child_instance_1.child_details()

