#program to find contact in a phone
ph_book={}
qurrey=[]
n=int(input())
for i in range(n):
    name=input()
    name=name.split(' ')
    ph_book[name[0]]=name[1]
try:
    q=input()
    qurrey.append(q)
except EOFError:
    pass
for m in qurrey:
    if m in ph_book:
        print(m,"=",ph_book[m])
    else:
        print('not found')
