import math as M
def isperfect(num):
    res=1
    sq=int(M.sqrt(num))
    for i in range(2,sq+1):
        if(num%i==0):
            res=res+i+(num//i)
            #print(i,num//i,res)
    return res==num
t=int(input())
while(t):
    num=int(input())
    res=isperfect(num)
    print(res)
    t=t-1
