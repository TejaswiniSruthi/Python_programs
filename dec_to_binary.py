t=int(input())
for _ in range(t):
    n=int(input())
    s=''
    while(n!=0):
        r=n%2
        s+=str(r)
        n//=2
    print(s[::-1])
