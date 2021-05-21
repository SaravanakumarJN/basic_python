number = int(input())

odd_sum = 0
for i in range(1, number+1):
    if i % 2 != 0: 
        odd_sum = odd_sum + i

print(odd_sum)