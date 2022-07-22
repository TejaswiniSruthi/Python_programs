def isspy(num):
    s=0
    m=1
    while(num):
        s+=(num%10)
        m*=(num%10)
        num=num//10
    return s==m

num=int(input())
res=isspy(num)
print(res)
