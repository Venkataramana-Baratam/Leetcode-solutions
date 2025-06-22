class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l1 = []
        res =0
        for i in range(0,len(s),k):
            l1.append(s[i:i+k])
        if len(l1[-1])<k:
            l1[-1] +=fill*(k-len(l1[-1]))
        return l1