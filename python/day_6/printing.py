# printing

## Embedding variables in string
### 1 Using Placeholders
'''
string      => %s
integer     => %d
float       => %f
'''
name = "Saravanakumar"
age = 22
print("I am %s and I am %d years old" %(name, age))

### 2 Using .format()
print("I am {} and I am {} years old" .format(name, age))



## sep - end 
### 1 sep
print("Karthi", "Sabari", "Dharanesh", sep=", ")

### 2 end
print("Karthi", "Sabari", "Dharanesh", end="\n")



## Joining list into string
array = [1, 2, 3, 4, 5]
print(*array)

