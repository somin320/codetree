rows = 4
cols = 4
matrix = [list(map(int, input().split())) for _ in range(rows)]
cnt = 0
for i in range(rows):
    for j in range(cols):
        if i >= j:
            cnt = cnt + matrix[i][j]
print(cnt)