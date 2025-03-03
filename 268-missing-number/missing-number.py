class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash = [0] * (n + 1)
        for i in range(n):
            hash[nums[i]] += 1
        for j in range(n + 1):
            if hash[j] == 0:
                return j
