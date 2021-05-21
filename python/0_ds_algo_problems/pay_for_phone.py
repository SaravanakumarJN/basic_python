price = list(map(int, input().strip().split()))
quantity = list(map(int, input().strip().split()))

total = 0
for i in range(len(price)):
    total += price[i] * quantity[i]

if total <= 150000:
    print("Possible")
else:
    print("Not Possible")