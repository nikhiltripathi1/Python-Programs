def solution(xs):
    xs.sort()
    o=0 #will check the presence of zero
    m=1 #multiplier
    n=[i for i in xs if i<0] #storing all negative power output
    if 0 in xs :
        o=1
    p=[j for j in xs if j>0] #storing all positive power output
    print(n,p,o,sep='\n')
    if len(n)==0 and len(p)==0:
        return 0
    elif len(n)==1 and len(p)==0:
        if o==1:
            return 0
        else :
            return n[0]
    else:
        if len(n)%2!=0:
            n.pop()
        for a in p:
            m*=a
        for a in n:
            m*=a
    return m
    
k=solution([2, 0, 2, 2, 0])
print(k)
            
    
    
    
    
