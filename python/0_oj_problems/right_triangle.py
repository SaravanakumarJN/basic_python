a, b, c = list(map(int, input().split()))

if a > b and a > c:
    if a**2 == ((b**2) + (c**2)):
        print("Yes")
    else:
        print("No")
elif b > a and b > c:
    if b**2 == ((a**2) + (c**2)):
        print("Yes")
    else:
        print("No")
elif c > a and c > a:
    if c**2 == ((a**2) + (b**2)):
        print("Yes")
    else:
        print("No")
else:
    print("No")
