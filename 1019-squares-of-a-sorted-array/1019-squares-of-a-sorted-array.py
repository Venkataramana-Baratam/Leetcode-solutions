
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        l, r = 0, n - 1
        pos = n - 1

        while l <= r:
            left_sq = nums[l] ** 2
            right_sq = nums[r] ** 2
            if left_sq > right_sq:
                result[pos] = left_sq
                l += 1
            else:
                result[pos] = right_sq
                r -= 1
            pos -= 1

        return result
