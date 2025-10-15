class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return 0
        end = [1]*n
        start = [1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                end[i] = end[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                start[i] =start[i+1]+1
        ans = 0
        for i in range(n-1):
            k = min(end[i], start[i + 1])
            ans = max(ans, k)
        return ans
        