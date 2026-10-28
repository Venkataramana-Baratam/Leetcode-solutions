class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        


        ans = [-1,-1]
        maxi = float('-inf')
        for i in range(len(nums)):

            for j in range(len(nums)):

                if i!=j and nums[i] + nums[j] == target and nums[i] > nums[j]:

                    product = nums[i] * nums[j]
                    if product > maxi:
                        maxi = product
                        ans = [i,j]

        return ans