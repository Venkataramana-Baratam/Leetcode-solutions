class Solution:
    def numSub(self, s: str) -> int:
        l = 0 
        r  =0 
        n =len(s)
        cnt = 0 
        while r<n:
            if s[r] =='1':
                l =r
            while r<n and s[r]=='1':
                cnt+=(r-l+1)
                r+=1
            r+=1
        return cnt % (10**9 + 7)