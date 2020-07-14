a=[]
for i in range(6):
    b=input()
    b=list(map(int,b.split(' ')))
    a.append(b)         
counter=[]
count=0
for k in range(4):
    for i in range(4):
        n=i
        for j in range(3):
            count+=a[k][n]
            n+=1
        counter.append(count)
        count=0
m=0        
for k in range(4):
    k+=2
    for i in range(4):
        n=i
        for j in range(3):
            count+=a[k][n]
            n+=1
        counter[m]+=count
        m+=1
        count=0
m=0
for k in range(4):
    k+=1
    for i in range(4):
        n=i+1
        counter[m]+=a[k][n]
        m+=1
        
print(max(counter))       
