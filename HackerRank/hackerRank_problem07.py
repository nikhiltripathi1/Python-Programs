time=input()
ntime=time.split(":")
a=ntime[2][2]+ntime[2][3]
ntime[2]=ntime[2][0]+ntime[2][1]
if a=='PM':
    ntime[0]=int(ntime[0])+12
    if ntime[0]==24:
        ntime[0]=12
else:
    if ntime[0]=='12':
        ntime[0]='00'
ntime[0]=str(ntime[0])    
time=":".join(ntime)
print(time)
