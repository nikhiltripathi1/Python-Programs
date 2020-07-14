n=int(input())
m=[]
count=0
counter=[]
while n!=0:
    k=n%16
    m.insert(0,str(k))
    n=n//16
print(m)    
print("".join(m))      

    
    
    
