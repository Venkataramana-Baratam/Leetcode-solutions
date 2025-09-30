class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            new_nums = list()
            for i in range(len(nums)//2):
                if i%2 ==0:
                    new_nums.append(min(nums[2*i],nums[2*i+1]))
                else:
                    new_nums.append(max(nums[2*i],nums[2*i+1]))
            nums = new_nums
        return nums[0]