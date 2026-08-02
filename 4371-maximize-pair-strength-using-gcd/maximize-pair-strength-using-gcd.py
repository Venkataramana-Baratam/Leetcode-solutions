import math

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxi = float('-inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                g = math.gcd(nums[i], nums[j])
                maxi = max(maxi, nums[i] * nums[j] // (g * g))

        return maxi