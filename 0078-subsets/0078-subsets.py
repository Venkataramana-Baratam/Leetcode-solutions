class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = 1<<len(nums)
        ans = []
        for num in range(subsets):
            list1 = [] 
            for i in range(len(nums)):
                if num &(1<<i):
                    list1.append(nums[i])
            ans.append(list1)
        return ans