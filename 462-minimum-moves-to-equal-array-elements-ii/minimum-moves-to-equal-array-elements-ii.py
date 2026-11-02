class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        middle = nums[n//2]

        cnt = 0
        for num in nums:
            cnt+=abs(middle - num)

        return cnt