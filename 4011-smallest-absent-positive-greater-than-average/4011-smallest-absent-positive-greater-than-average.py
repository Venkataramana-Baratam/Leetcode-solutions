from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        present = set(nums)
        
        candidate = int(avg) + 1  
        while True:
            if candidate not in present:
                return candidate
            candidate += 1
