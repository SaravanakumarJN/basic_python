# lists or Arrays
array = [1, 2, 3, 4, 5]

# positive indexing
print(array[1])

# refers to last index and goes in that fashion
print(array[-1])

# slice  [start_index : untill_index(optional)]
# start included but end not included
print(array[2 : ])
print(array[2 : 4])

# accessing individual elements by iterating in array
for i in array:
    print(i)

# list methods 

# append method (add to end)
array.append(-10)
print(array)

# sort method
array.sort()
print(array)

# find element in array
to_find = 5
if to_find in array:
    print("Yes")
else:
    print("No")


