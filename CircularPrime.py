from math import sqrt

def prime(n):
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=input()
l=len(n)
if prime(int(n)):
    f=True
    for i in range(l-1):
        nn=''
        nn=n[1:l]+n[0]
        if not(prime(int(nn))):
            print('prime but not a circular prime')
            f=False
            break
    if f:
        print('circular prime')
else:
    print('not prime')
