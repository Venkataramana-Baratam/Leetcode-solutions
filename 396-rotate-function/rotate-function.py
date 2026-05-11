class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        n  = len(nums)

        total_sum = sum(nums)

        curr = 0
        for i,num in enumerate(nums):

            curr += num * i

        maxi = curr

        for k in range(1,n):

            curr = curr + total_sum - n * nums[-k]
            maxi = max(maxi,curr)

        return maxi