rows, cols = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(rows)]
matrix2 = [list(map(int, input().split())) for _ in range(rows)]

for i in range(rows):
    new_row = []
    for j in range(cols):
        if matrix1[i][j] == matrix2[i][j]:
            new_row.append(0)
        else:
            new_row.append(1)
    print(*new_row)