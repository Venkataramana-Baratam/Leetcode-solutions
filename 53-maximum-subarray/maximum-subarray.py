class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=nums[0]
        for num in nums:
            sum=sum+num
            maxi = max(maxi,sum)
            if sum<0:
                sum=0
        return maxi