class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            k=nums[i]
            for j in range(i+1,len(nums)):
                if k+nums[j]==target:
                    return [i,j]