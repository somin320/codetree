rows = 4
cols = 4
matrix = [list(map(int, input().split())) for _ in range(rows)]
cnt = 0
for i in range(rows):
    for j in range(cols):
        if i < j or (i == 0 and j == 0) or (i == 3 and j == 3):
            cnt = cnt + matrix[i][j]
print(cnt)