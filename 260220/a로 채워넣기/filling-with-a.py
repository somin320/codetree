arr = list(input())
n = len(arr)
arr[1] = 'a'
arr[n-2] = 'a'
print("".join(arr))