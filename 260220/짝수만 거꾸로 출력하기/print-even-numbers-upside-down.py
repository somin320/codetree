n = int(input())
arr = list(map(int, input().split()))
for i in range(n): arr[i]
for num in arr[::-1]:
    if num % 2 == 0: print(num, end = " ")