q=int(input())
for _ in range(q):
    n=int(input())
    bin=""
    i=s=0
    while(n!=0):
        r=n%10
        s+=r*(pow(8,i))
        n=n//10
        i+=1
    while(s!=0):
        r=s%2
        bin+=str(r)
        s=s//2
    print(int((bin)[::-1]))
