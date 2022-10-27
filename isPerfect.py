from math import sqrt

def isperfect(num):
    res=1
    for i in range(2,int(sqrt(num))+1):
        if(num%i==0):
            if((num//i)==i):
                continue
            res=res+i+(num//i)
    return res==num

num=int(input())
print(isperfect(num))
