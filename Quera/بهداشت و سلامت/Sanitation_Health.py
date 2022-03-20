X = int(input())
N = int(input())

if N==0:
    grade = 20
elif N==7:
    grade = X
else:
    grade = X - N
    if grade<0:
        grade = 0

print(grade)
