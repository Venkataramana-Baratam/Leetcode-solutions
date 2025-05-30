class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])