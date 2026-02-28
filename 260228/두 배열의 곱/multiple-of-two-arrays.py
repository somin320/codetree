rows = 3
cols = 3
matrix1 = [list(map(int, input().split())) for _ in range(rows)]
input()
matrix2 = [list(map(int, input().split())) for _ in range(rows)]

for i in range(rows):
    new_row = []
    for j in range(cols):
        new_row.append(matrix1[i][j] * matrix2[i][j])
    print(*new_row)