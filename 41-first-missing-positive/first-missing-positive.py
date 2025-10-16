class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)   
        i = 1
        while True:
            if i not in nums:
                return i
            i += 1
