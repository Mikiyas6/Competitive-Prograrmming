class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 0
        storing_allprevious_factorial=[0]*n
        storing_allprevious_factorial[0]=1
        storing_allprevious_factorial[1]=1
        for i in range(2,n):
            storing_allprevious_factorial[i]=storing_allprevious_factorial[i-1]*i
        value=storing_allprevious_factorial[-1]*n
        count = 0
        ans=str(value)
        i=len(ans)-1
        while ans[i]=="0":
            count+=1
            i-=1
        return count
        