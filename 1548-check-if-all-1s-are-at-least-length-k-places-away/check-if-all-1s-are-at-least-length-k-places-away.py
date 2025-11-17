class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        l = 0
        r = 0
        n = len(nums)

        while l < n and nums[l] != 1:
            l += 1

        if l == n:  
            return True

        r = l + 1

        while r < n:
            while r < n and nums[r] != 1:
                r += 1

            if r < n:  
                if (r - l - 1) < k:
                    return False
                l = r

            r += 1

        return True
