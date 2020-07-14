def solution(l):
    count=0
    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            if l[j]%l[i]==0:
                for k in range(j+1,len(l)):
                    if l[k]%l[j]==0:
                        count=count+1
    return count

k=solution([i for i in range(1,2001)])
print(k)


