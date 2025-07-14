class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])
        for subarray in nums[1:]:
            common = common & set(subarray)
        ans = list(common)
        ans.sort()
        return ans