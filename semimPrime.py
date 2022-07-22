def semiPrime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count==1 or count==2):
        return True
    elif(count>2 or count==0):
        return False
n=int(input())
res=semiPrime(n)
print(res)
