class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if any(i==1 for i in nums):
            return n - nums.count(1)
        
        min_len = float('inf')
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i+1,len(nums)):
                g = math.gcd(g,nums[j])
                if g==1:
                    min_len = min(min_len,j-i+1)
                    break
        if min_len == float('inf'):
            return -1
        
        return n+min_len - 2
