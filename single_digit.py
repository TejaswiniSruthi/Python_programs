n=int(input())
ar1=list(map(int,input().split()))
ar2=[]
s=0
for i in ar1:
    if i not in ar2:
        ar2.append(i)
    else:
        s+=i
print(sum(ar2)-s)
