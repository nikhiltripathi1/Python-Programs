def solution(n,b):
    res=[]
    while(n not in res) :
        res.append(n)
        N=list(map(int,[i for i in n]))
        x=N[:]
        x.sort(reverse=True)
        y=N[:]
        y.sort()
        numx,numy=0,0
        for i in range(len(N)):
            numx+=x[-1*(i+1)]*(b**i)
            numy+=y[-1*(i+1)]*(b**i)
        z=numx-numy
        c=[]
        while(z!=0):
            c.insert(0,z%b)
            z=z//b
        if len(c)!=len(N):
            for i in range(len(N)-len(c)):
                c.insert(0,0)
        c=list(map(str,c))
        n="".join(c)
    res.append(n)
    for i in range(len(res)):
        if n==res[i]:
            return len(res)-i-1
k=solution('1211',10)
print(k)                
    
