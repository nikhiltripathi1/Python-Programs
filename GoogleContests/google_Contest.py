t=int(input())
for i in range(t):
    task=int(input())
    acty=[]
    res=["J"]
    for j in range(task):
        start,end=input().split()
        start,end=int(start),int(end)
   
        acty.append([start,end])
       
    for j in range(task-1):
        if acty[j][1]-acty[j+1][0]<=0:
            res.append("J")
        else:
            res.append("C")
    #else:
        #res=["IMPOSSIBLE"]
    
    
    res="".join(res)
    print("Case #",i+1,": ",res,sep="")
            

    
        
