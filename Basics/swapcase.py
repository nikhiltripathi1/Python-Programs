s='AAaa'
s=list(s)
n=[]
for i in s:
    if i.islower():
        i=i.upper()
    elif i.isupper():
        i=i.lower()
    n.append(i)   
n=''.join(n)
print(n)
