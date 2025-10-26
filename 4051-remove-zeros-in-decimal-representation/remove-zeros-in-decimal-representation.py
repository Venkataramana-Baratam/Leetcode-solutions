class Solution:
    def removeZeros(self, n: int) -> int:
        ans = ""
        for i in str(n):
            if i!='0':
                ans+=i
        return int(ans)