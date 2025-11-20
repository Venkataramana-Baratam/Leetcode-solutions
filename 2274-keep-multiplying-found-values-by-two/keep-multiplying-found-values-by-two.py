class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        while original in nums:
            original = original*2
        return original