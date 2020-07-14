print('''
       -----------------------
       |                     |
       |                     |
       |    0          0     |
       |         <           |
       |    ,          ,     |
       |      ,______,       |
       |                     |
       -----------------------
       ''')
num=int(input("enter no.:"))
def fac(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fac(num-1)
      
factorial=fac(num)
print("factorial of ",num," is ",factorial)
input()
