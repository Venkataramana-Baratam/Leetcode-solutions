class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        min_num = min(nums)
        return k*(max_num - min_num)