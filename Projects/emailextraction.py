import re
pattern=r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>'
n=int(input())
for i in range(n):
    stri=input()
    x,y=stri.split(' ')
    match=re.findall(pattern,y)
    if match:
        print(x,y)
