size=5
counter=3
n=0
k=4
array=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for m in range(3):
    for i in range(size):
        for j in range(size):
            if i==n or j==k or i==k or j==n:
                if array[i][j]==0:
                    array[i][j]=counter
    n+=1
    k-=1
    counter-=1

for i in range(size):
    print(array[i][0]," ",array[i][1]," ",array[i][2]," ",array[i][4]," ",array[i][4]," ")    
    
