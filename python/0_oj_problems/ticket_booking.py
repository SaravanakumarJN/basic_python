price = list(map(int, input().strip().split()))
no_of_tickets = list(map(int, input().strip().split()))

total = 0
for i in range(len(price)):
    total += price[i] * no_of_tickets[i]

print(total)