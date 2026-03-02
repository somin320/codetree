# 1. 4개의 줄에 데이터가 들어오므로 rows를 4로 설정합니다.
rows = 4

# 2. 2차원 리스트로 데이터를 입력받습니다.
matrix = [list(map(int, input().split())) for _ in range(rows)]

# 3. 각 행(row)을 돌면서 합계를 구해 출력합니다.
for row in matrix:
    # sum() 함수를 사용하면 리스트 안의 숫자를 모두 더해줍니다.
    print(sum(row))