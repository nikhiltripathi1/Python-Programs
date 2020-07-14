t=int(input())
for i in range(t):
    string=input()
    count=0
    newstr=[]
    string=list(int(s) for s in string)
    count=string[0]
    newstr.append(string[0]*"(")
    newstr.append(str(string[0]))
       
    for a in range(len(string)-1):
        d=string[a]-string[a+1]
        if d<0 :
            d*=-1
            count+=d
            newstr.append(d*"(")
            newstr.append(str(string[a+1]))
        elif d>0 :
            count-=d
            newstr.append(d*")")
            newstr.append(str(string[a+1]))
        else:
            newstr.append(str(string[a+1]))
    newstr.append(count*")")
    newstr="".join(newstr)
    print("Case #",i+1,": ",newstr)
            
        
        
