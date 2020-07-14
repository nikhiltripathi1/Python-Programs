import numpy as np
t=int(input())
for m in range(t):
    n=int(input())
    arr=[]
    k=0
    r=0
    c=0
    for a in range(n):
        value=input()[0:2*n-1]
        arr.append(list(map(int,value.split(" "))))
    
    for i in range(n):
        for j in range(n):
            if i==j:
                k+=arr[i][j]
    duparr=arr[:]
    duparr=list(list(set(s)) for s in duparr)
    for s in duparr:
        if len(s)<n:
            r+=1
    arr=np.array(arr)
    arr=arr.transpose()
    arr=list(list(u) for u in arr)
    duparr=arr[:]
    duparr=list(list(set(s)) for s in duparr)
    for s in duparr:
        if len(s)<n:
            c+=1
    print("case #",m+1,": ",k," ",r," ",c,sep="")
    
