sex = int(input())
age = int(input())
if age >= 19:
    if sex == 1:
        print("WOMAN")
    elif sex == 0:
        print("MAN")
else:
    if sex == 1:
        print("GIRL")
    elif sex == 0:
        print("BOY")