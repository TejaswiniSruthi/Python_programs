import math
def sfac(n,i,s):
    sq=int(math.sqrt(n))
    if(sq==i):
        if(sq*sq==n):
            return s-sq
        else:
            return s
    if(n%i==0):
        s+=(i+n//i)
        i+=1
        return sfac(n,i,s)
    else:
        i+=1
        return sfac(n,i,s)

n=int(input())
s=0
i=1
res=sfac(n,i,s)
print(res)
