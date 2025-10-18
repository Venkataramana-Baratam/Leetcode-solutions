class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        next_available = -float('inf')
        count= 0
        for num in nums:
            assigned = max(next_available,num-k)
            if assigned<=num+k:
                count+=1
                next_available = assigned+1
        return count
