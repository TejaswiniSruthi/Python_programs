        n=len(s)-1
        for i in range(n):
            s[i],s[n]=s[n],s[i]
            n-=1
            if(i==n or i>n):
                break
