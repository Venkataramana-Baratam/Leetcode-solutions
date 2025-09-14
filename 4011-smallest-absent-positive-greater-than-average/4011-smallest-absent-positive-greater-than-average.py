class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        arr_sum = sum(nums)
        avg = arr_sum/n
        for i in range(1,150):
            if i>avg and i not in nums:
                return i