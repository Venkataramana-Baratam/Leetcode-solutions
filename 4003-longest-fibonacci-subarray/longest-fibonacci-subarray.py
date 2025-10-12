class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        maxi = 2
        current= 2
        for i in range(2,n):
            if nums[i] == nums[i-1] + nums[i-2]:
                current+=1
            else:
                current = 2
            maxi = max(maxi,current)
        return maxi