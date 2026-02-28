rows = 3
cols = 3
matrix = [list(map(int, input().split())) for _ in range(rows)]
new_matrix = []
for i in range(rows):
    new_row = []
    for j in range(cols):
        new_row.append(matrix[i][j] * 3)
    new_matrix.append(new_row)
for row in new_matrix:
    print(*row)