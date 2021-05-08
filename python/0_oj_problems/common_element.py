array1 = {1, 2, 3}
array2 = {4, 3, 5}

# print(*array1.intersection(array2))

for i in array1:
    if i in array2:
        print(i)

# intersection = []
# for i in array1:
#     for j in array2:
#         if i == j:
#             intersection.append(i)

# print(intersection)
