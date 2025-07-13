class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans =0
        j =0 
        for i in range(len(g)):
            while j<len(s):
                if s[j]>=g[i]:
                    ans+=1
                    j+=1
                    break
                j+=1
        return ans