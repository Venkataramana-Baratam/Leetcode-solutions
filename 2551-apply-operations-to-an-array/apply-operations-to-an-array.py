from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Modify elements based on adjacent equality
        for i in range(len(nums) - 1):  # Fix: stop at len(nums)-2
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        # Move non-zero elements to the front
        j = 0  # Initialize j to 0 to keep track of non-zero positions
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]  # Swap non-zero element with zero
                j += 1  # Move to next position for non-zero elements
                
        return nums
