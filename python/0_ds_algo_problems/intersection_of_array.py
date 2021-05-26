n = int(input())
array1 = list(input().strip().split(" "))
array2 = list(input().strip().split(" "))

found = False
intersection = ""
for ele1 in array1:
    for ele2 in array2:
        if ele1 == ele2:
            intersection = ele1
            found == True
            break
    if found:
        break

print(intersection)

