class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pf=0
        max_pf=0
        pf =0
        for num in nums:
            pf+=num
            min_pf =min(min_pf,pf)
            max_pf = max(max_pf,pf)
        return max_pf-min_pf