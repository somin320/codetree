n = int(input())
numbers = list(map(int, input().split()))
arr_numbers = []
for x in numbers:
    arr_numbers.append(x*x)
print(*arr_numbers)