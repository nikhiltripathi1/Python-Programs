a=[]
def sorting(val):
    return val[1]
def namesort(val):
    return val[0]
n=int(input())
for i in range(n):
    b=[]
    name=input()
    score=float(input())
    b.append(name)
    b.append(score)
    a.append(b)
c=[]
a.sort(key=sorting)
secsmall=a[0][1]
for i in a:
    if i[1]==secsmall:
        continue
    else:
        secsmall=i[1]
        break
for i in a:
    if i[1]==secsmall:
        c.append(i)
c.sort(key=namesort)        
for i in c:
    print(i[0])
       

        
        
