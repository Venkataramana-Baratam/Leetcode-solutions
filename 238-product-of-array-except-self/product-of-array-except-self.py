class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        n = len(nums)

        ans = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        # full prefix products including self
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]

        # full suffix products including self
        suffix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        # build answer using prefix and suffix

        if n == 1:
            return [1]

        # i = 0 → product of nums[1..]
        ans[0] = suffix[1]

        # 0 < i < n-1 → prefix before i * suffix after i
        for i in range(1, n-1):
            ans[i] = prefix[i-1] * suffix[i+1]
        ans[n-1] = prefix[n-2]

        return ans
