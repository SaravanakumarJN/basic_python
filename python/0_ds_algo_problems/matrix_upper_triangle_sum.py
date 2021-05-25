rows = int(input())

matrix = []
for i in range(rows):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

sum = 0
for i in range(len(matrix)):
    j = 0
    while j <= (len(matrix[i]) - 1 - i):
        sum += matrix[i][j]
        j += 1

print(sum)