class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res  = 1
        d = nums[0]
        for num in nums:
            if num - d>k:
                res+=1
                d = num
        return res