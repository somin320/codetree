n = int(input())
for i in range(n, 101):
    if i >= 90: result = "A"
    elif i >= 80: result = "B"
    elif i >= 70: result = "C"
    elif i >= 60: result = "D"
    else: result = "F"
    print(result, end=" ")