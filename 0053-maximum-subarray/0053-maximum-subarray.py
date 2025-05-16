class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxi = -sys.maxsize-1
        for num in nums:
            sum+=num
            if sum<0:
                sum=0
            if sum>maxi:
                maxi = sum
        return maxi