n=int(input())
arr=list(map(int,input().split()))[:n]
min=arr[0]
for i in arr:
    if(i<min):
        min=i
print(min)
