def dec_bin(n):
    s=''
    while(n!=0):
        r=n%2
        s+=str(r)
        n//=2
    print(int(s[::-1]))

t=int(input())
for _ in range(t):
    n=(input())
    l=len(n)-1
    r=0
    for i in n:
        r+=int(i)*(8**l)
        l-=1
    dec_bin(r)
