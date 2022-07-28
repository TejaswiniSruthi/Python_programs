def func(a,b):
    if(a==1):
        return b
    if a%2:
        return b+func(a//2,b*2)
    else:
        return func(a//2,b*2)
a=int(input())
b=int(input())
res=func(a,b)
print(res)
