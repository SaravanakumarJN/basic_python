rows = int(input())

matrix = []
for i in range(rows):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

d1_sum = 0
d2_sum = 0
for i in range(len(matrix)):
    d1_sum += matrix[i][i]
    d2_sum += matrix[i][len(matrix) - 1 - i]

diff_of_diagonal = d1_sum - d2_sum
print(diff_of_diagonal)