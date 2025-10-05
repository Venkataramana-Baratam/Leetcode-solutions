class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even_ind_sum =0 
        odd_ind_sum = 0
        n = len(nums)
        for i in range(0,n,2):
            even_ind_sum+=nums[i]
        for i in range(1,n,2):
            odd_ind_sum+=nums[i]
        return even_ind_sum - odd_ind_sum