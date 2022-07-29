def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,b%a)

def lcm(a,b):
    return a*b//gcd(a,b)

a=int(input())
b=int(input())
res=lcm(a,b)
print("lcm:",res)
result=gcd(a,b)
print("gcd:",result)
