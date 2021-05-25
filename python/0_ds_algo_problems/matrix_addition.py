m1 = int(input())

matrix1 = []
for i in range(m1):
    row = list(map(int, input().strip().split()))
    matrix1.append(row)

m2 = int(input())

matrix2 = []
for i in range(m2):
    row = list(map(int, input().strip().split()))
    matrix2.append(row)

result_matrix = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[i])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(row)

print(result_matrix)