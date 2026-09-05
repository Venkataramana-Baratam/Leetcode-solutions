class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        total = 0
        maxi = float('-inf')

        for num in nums:

            total+=num

            if total > maxi:

                maxi = total

            if total < 0:
                total = 0

        return maxi