n = int(input())
total_sum = 0
count = 0
while True:
    count += 1
    total_sum += count
    if total_sum >= n:
        print(count)
        break
    else: continue