t=int(input())
for _ in range(t):
    n=(input())
    l=len(n)-1
    r=0
    for i in n:
        r+=int(i)*(2**l)
        l-=1
    print(r)
