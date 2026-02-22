sum_three = 0
sum_five = 0
for _ in range(10):
    num = int(input())
    if num % 3 == 0:
        sum_three += 1
    if num % 5 == 0:
        sum_five += 1
print(sum_three, sum_five)