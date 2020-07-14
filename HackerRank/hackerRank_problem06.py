a=int(input())
string=[]
deletion=[]
for i in range(a):
    string.append(input())
    delete=0
    n=1
    for l in string[i]:
        if string[i][n]==l:
            delete+=1
        n+=1
        if n==len(string[i]):
            break
    deletion.append(delete)
for i in range(a):
    print(deletion[i])


