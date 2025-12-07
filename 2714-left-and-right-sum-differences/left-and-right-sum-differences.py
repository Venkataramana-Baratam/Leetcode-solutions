class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n 
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        suffix = [0] * n
        suffix[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] + nums[i]
        ans =[0] * n
        for i in range(n):

            ans[i] = abs(prefix[i] - suffix[i])
        return ans