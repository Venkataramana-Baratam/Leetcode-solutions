from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        present = set(nums)
        candidate = max(1,int(avg) + 1)  
        while True:
            if candidate not in present:
                return candidate
            candidate += 1
