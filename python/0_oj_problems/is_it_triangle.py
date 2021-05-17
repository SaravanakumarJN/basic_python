def triangle_check(sides):
    is_triangle = False
    if (sides[0] < sides[1] + sides[2]) and (sides[1] < sides[0] + sides[2]) and (sides[2] < sides[1] + sides[0]):
        is_triangle = True
    return is_triangle

tc = int(input())

for i in range(tc):
    array = list(map(int, input().strip().split(" ")))
    
    if triangle_check(array):
        print("Yes")
    else:
        print("No")
