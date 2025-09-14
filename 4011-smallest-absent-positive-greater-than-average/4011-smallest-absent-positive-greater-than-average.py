class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        arr_sum = sum(nums)
        avg = arr_sum/n
        i = int(avg)+1
        while True:
            if i not in nums:
                return i
            i+=1