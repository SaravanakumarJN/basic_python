rows = int(input())

matrix = []
for i in range(rows):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

for j in range(len(matrix[0])):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][j]
    print(sum)


