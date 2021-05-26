num1, num2 = list(map(int, input().strip().split(" ")))

high = max(num1, num2)
low = min(num1, num2)

recent_divisor = 1
for i in range(1, low):
    if(num1 % i == 0 and num2 % i == 0):
        recent_divisor = i

print(recent_divisor)