# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
A=input().split(' ')
b=int(input())
B=input().split(' ')
c=set(A).union(set(B))
d=set(B).intersection(set(A))
res=c.difference(d)
for i in range(len(res)):
   print(min(res))
   res.remove(min(res))
