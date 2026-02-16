sex = input()
age = int(input())
if age >= 19:
    if sex == 1:
        print("Woman")
    elif sex == 0:
        print("Man")
else:
    if sex == 1:
        print("Girl")
    elif sex == 0:
        print("Boy")