rows = int(input())

matrix = []
for i in range(rows):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

start_row, start_column = map(int, input().strip().split())
end_row, end_column = map(int, input().strip().split())

result_matrix = []
for i in range(start_row, end_row + 1):
    row = []
    for j in range(start_column, end_column + 1):
        row.append(matrix[i][j])
    result_matrix.append(row)

print(result_matrix)