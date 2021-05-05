a, c, b = input().split()
a = int(a)
b = int(b)

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
else:
    print(a / b)