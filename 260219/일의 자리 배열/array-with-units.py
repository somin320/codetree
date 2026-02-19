arr = list(map(int, input().split()))
for i in range(8):
    sum_val = arr[-1] + arr[-2]
    arr.append(sum_val % 10)
print(*arr)