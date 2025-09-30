class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            nums = self.new_arr(nums)
        return nums[0]
    def new_arr(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            res.append((nums[i]+nums[i+1])%10)
        return res