l=input()
h=l.split(' ')
s=int(h[0])
t=int(h[1])
del h
c=input()
h=c.split(' ')
a=int(h[0])
b=int(h[1])
del h
k=input()
h=k.split(' ')
m=int(h[0])
n=int(h[1])
del h
array=input()
arraym=array.split(' ')
countm=0
for i in range(m):
    arraym[i]=int(arraym[i])
    if arraym[i]>0:
        d=a+arraym[i]
        if d>=s and d<=t:
            countm+=1
array=input()
arrayn=array.split(' ')
countn=0
for i in range(n):
    arrayn[i]=int(arrayn[i])
    if arrayn[i]<0:
        d=b+arrayn[i]
        if d>=s and d<=t:
            countn+=1
print(countm)
print(countn)
    
