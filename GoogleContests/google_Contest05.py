# Enter your code here. Read input from STDIN. Print output to STDOUT
k,m=map(int,input().split(' '))
maximum=[]
for i in range(k):
    a=list(map(int,input().split(' ')))
    a=max(a)**2
    maximum.append(a)
s=sum(maximum)
print(s%m)    
