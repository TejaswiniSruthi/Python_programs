dic={'0':'01','1':'10'}
a,b=map(int,input().split())
a1='0'
for _ in range(a-1):
    a2=''
    for i in a1:
        a2=a2+dic[i]
        a1=a2
print(a1[b-1])
