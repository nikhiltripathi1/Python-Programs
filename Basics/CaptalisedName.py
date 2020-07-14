s=input()
s=s.split(' ')
a=[]
for i in s:
    i=list(i)

    i[0]=i[0].upper()
    i=''.join(i)

    a.append(i)
a=' '.join(a)
print(a)
