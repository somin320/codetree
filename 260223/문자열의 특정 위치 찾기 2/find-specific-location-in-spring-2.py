words = ["apple", "banana", "grape", "blueberry", "orange"]
s = input()
cnt = 0
for word in words:
    if word[2] == s or word[3] == s:
        print(word)
        cnt += 1
print(cnt)