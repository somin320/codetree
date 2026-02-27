start, end = map(int, input().split())
ans_count = 0
for n in range(start, end + 1):
    divisor_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_count += 1
    if divisor_count == 3:
        ans_count += 1
print(ans_count)