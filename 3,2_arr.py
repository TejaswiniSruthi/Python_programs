n=int(input())
arr=list(map(int,input().split()))
res=0
for i in arr:
    if(i==3):
        res+=1
    else:
        break
print(n-res)
