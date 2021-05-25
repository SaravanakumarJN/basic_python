rows = int(input())

matrix = []
for i in range(rows):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

sum = 0
for i in range(rows):
    for j in range(len(matrix[i])):
        sum += matrix[i][j]

print(sum)