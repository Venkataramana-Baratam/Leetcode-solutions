class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        maxi = 0
        for i in range(n):
            mpp = {}
            for j in range(i,n):
                mpp[s[j]] = mpp.get(s[j],0)+1
                if len(set(mpp.values()))==1:
                    maxi = max(maxi,j-i+1)
        return maxi