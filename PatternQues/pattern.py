a='---'
b='.|.'
c='WELCOME'
n=int(input())
k=(n-1)//2
l=1
for i in range((n-1)//2):
    print(a*k+b*l+a*k)
    k-=1
    l+=2
m=(n*3-9)//6    
print(a*m+'-'+c+'-'+a*m)
k=1
l=n-2
for i in range((n-1)//2):
    print(a*k+b*l+a*k)
    k+=1
    l-=2
