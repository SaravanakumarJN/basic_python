# Immutables
'''
integer
string
tuple       ** similar to list only difference is it's immutable
set
'''

# Mutables
'''
list
dictionary
'''

# checking whether mutable or not
string = "abc"
print(id(string))
string = "abcd"
print(id(string))

float1 = 1.22
print(id(float1))
float1 = 1.33
print(id(float1))
