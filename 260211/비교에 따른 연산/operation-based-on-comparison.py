a, b = map(int, input().split())
if a > b:
    print(a*b)
else:
    print(f"{b/a:.0f}")