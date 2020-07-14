def solution(l):
    count=0
    L=list(set(l))
    l.sort(reverse=True)
    L.sort(reverse=True)
    for i in range(len(L)):
        c=[]
        r=L[i]
        l.remove(l[0])
        m=[j for j in l if j==L[i] or j<=L[i]//2]
        for j in range(len(m)):
            if L[i]%m[j]==0:
                c.append(m[j])
        R=[]
        print(m,'\n',c)
        for i in range(len(c)):
            A=[]
            for j in range(i,len(c)):
                      if c[i]%c[j]==0:
                            A.append(c[j])
            A=list(set(A))
            print(A)
            R.append(A)
        R.sort()
        k=R
        R=[k[i] for i in range(len(k)) if i==0 or k[i]!=k[i-1]]
        for j in range(len(R)):
            if l.count(R[j][-1])>1 :
                 count=count+len(R[j])
            else:
                count=count+len(R[j])-1
        print('\n\n',r)
        l=[g for g in l if g!=r]
        print(l)
    return count
d=[b for b in range(1,10)]
k=solution([9,3,1])
print(k)
