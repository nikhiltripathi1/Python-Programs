#program to reverse an array
n = int(input())
arr=input()
arr=arr.split(' ')

narr=[]
m=-1
for i in range(n):
    narr.append(arr[m])
    m-=1
narr=' '.join(narr)
print(narr)
