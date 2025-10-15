from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        check = [False] * n

        # Step 1: Check all subarrays of length k
        for i in range(n - k + 1):
            for j in range(i + 1, i + k):
                if nums[j] <= nums[j - 1]:
                    break
            else:
                check[i] = True
        for i in range(n - k):
            if check[i] and check[i + k]:
                return True

        return False
