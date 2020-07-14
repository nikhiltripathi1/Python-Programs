take=[]
pos=[]
big=0
score=[]
n=int(input("enter no. of columns:"))
for i in range(n):
    a=int(input())
    take.append(a)
    pos.append(i+1)
print(take)
print(pos)
for k in range(n):
    for i in range(n):
        if big<take[i]+pos[i]:
            big=take[i]+pos[i]
    score.append(big)
    b=pos[0]
    for i in range(n-1):
        pos[i]=pos[i+1]
    pos[n-1]=b
print(score)
