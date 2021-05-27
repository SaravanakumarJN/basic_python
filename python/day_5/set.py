# set (can contain only distinct element) [Note : unordered]

## initialise set 
set1 = { 2, 3, 1, 3, 4, 2, 1}         # stores only distinct element
print(set1)


## add element to end of set
### 1 using add
set2 = set()
set2.add(1)
set2.add(2)
print(set2)

### 2 using update [Note : used to multiple element in one go. So takes a array as input]
set2.update([1, 2, 3, 4])
print(set2)


## remove element from set
### 1 using remove (remove throws error if the elemnet to removed is not present)
set1.remove(2)
print(set1)

### 2 using discard (discard doesn't throws error if the elemnet to removed is not present)
set1.discard(10)
print(set1)


## union and intersection of set
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7, 8}
union = set.union(set_1, set_2)
intersect = set.intersection(set_1 , set_2)
print(union)
print(intersect)


## difference of set  (gives the difference of two set (note : will give only the first set elements))
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 6, 7}
print(set1.difference(set2))


## symmetric difference of set ( (gives the difference of two set (note :  will give elements not found in both set)))
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 6, 7}
print(set1.symmetric_difference(set2))


## check disjoint sets  (returns true if both sets have no common element in them, else returns false)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))

set1 = {1, 2, 3}
set2 = {1, 5, 6}
print(set1.isdisjoint(set2))


## check subset or not
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4}
print(set2.issubset(set1))

set1 = {1, 2, 3, 4, 5}
set2 = {0, 2, 4}
print(set2.issubset(set1))


## check superset or not
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3}
print(set1.issuperset(set2))

set1 = {0, 2, 3, 4}
set2 = {1, 2, 3}
print(set1.issuperset(set2))


## typecasting list to set
list = [1, 2, 1, 2, 3, 4, 3, 4]
distinct_ele_list = set(list)
print(distinct_ele_list)

