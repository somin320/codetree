num1, num2, num3 = map(int, input().split())
total = num1 + num2 + num3
average = total / 3
print(total)
print(f"{average:.0f}")
print(f"{total - average:.0f}")