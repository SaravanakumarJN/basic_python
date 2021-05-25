def sum_of_matrix(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]

    return sum

m1_rows, m1_cols = map(int, input().strip().split())
m1 = []
for i in range(m1_rows):
    row = list(map(int, input().strip().split()))
    m1.append(row)

m2_rows, m2_cols = map(int, input().strip().split())
m2 = []
for i in range(m2_rows):
    row = list(map(int, input().strip().split()))
    m2.append(row)

m1_sum = sum_of_matrix(m1)
m2_sum = sum_of_matrix(m2)

print(max(m1_sum, m2_sum))