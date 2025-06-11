class Solution:
    def maxDifference(self, s: str) -> int:
        mpp = {}
        for i in s:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        maxiodd = 0
        minieven = float('inf')
        for key,value in mpp.items():
            if value%2!=0:
                maxiodd = max(maxiodd,value)
            else:
                minieven = min(minieven,value)
        return maxiodd-minieven