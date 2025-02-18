class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l1 =[]
        low = 0
        high = len(s)
        for i in range(len(s)):
            if s[i]=='I':
                l1.append(low)
                low=low+1
            elif s[i]=='D':
                l1.append(high)
                high = high-1
            if low==high:
                l1.append(low)
        return l1