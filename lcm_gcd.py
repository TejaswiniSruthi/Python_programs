def lcm(a,b):
    rem=1
    while(rem):
        rem=a%b
        a=b
        b=rem
    return a

a=int(input())
b=int(input())
res=lcm(a,b)
print("lcm:",res)
