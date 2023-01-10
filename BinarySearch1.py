class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        l=0
        r=N
        while(l<=r):
            m=(l+r)//2
            if arr[m]==K:
                return 1
            if arr[m]>K:
                r=m-1
            else:
                l=m+1
        return -1
