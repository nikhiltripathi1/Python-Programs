a=int(input())
grade=[]
for i in range(a):
    grade.append(int(input()))
    if grade[i]>=38:
        d=5-(grade[i]%5)
        if d<3:
            grade[i]+=d
for i in range(a):
    print(grade[i])
