3c='-'
n=int(input())
p=[]
k=96+n
m=2*n-2
for i in range(n):
    h=list(chr(j)+c for j in range(k,k-i-1,-1))
    g=list(chr(j)+c for j in range(k-i+1,k+1))
    g=''.join(g)
    h="".join(h)
    h=h+g
    p.append(c*m+h+c*(m-1))
    m-=2
p[n-1]=list(p[n-1])
p[n-1].pop()
p[n-1]=''.join(p[n-1])
for i in range(n-2,-1,-1):
    p.append(p[i])
for i in p:
    print(i)
    
