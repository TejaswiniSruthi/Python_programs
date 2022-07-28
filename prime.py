def prime(n,i):
    if(n%i==0):
        return False
    else:
        i+=1
        if(i==n):
            return True
        else:
            return prime(n,i)

n=int(input())
i=2
res=prime(n,i)
print(res)
