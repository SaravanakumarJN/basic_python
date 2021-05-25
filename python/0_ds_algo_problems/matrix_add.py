def matrix_addition(matrix1, matrix2):
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        print(*row)
        result_matrix.append(row)
    


m1_rows, m1_cols, m2_rows, m2_cols = map(int, input().strip().split())

if m1_rows == m2_rows and m1_cols == m2_cols:
    m1 = []
    for i in range(m1_rows):
        row = list(map(int, input().strip().split()))
        m1.append(row)

    m2 = []
    for i in range(m2_rows):
        row = list(map(int, input().strip().split()))
        m2.append(row)

    matrix_addition(m1, m2)
    
else:
    print("-1")