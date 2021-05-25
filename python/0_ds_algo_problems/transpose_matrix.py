rows = int(input())

matrix = []
for i in range(rows):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

transposed_matrix = []
for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transposed_matrix.append(row)

print(transposed_matrix)