class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        seen = {}
        l = 0
        n = len(nums)
        ans = float('inf')
        dist_sum = 0

        for r in range(n):
            seen[nums[r]] = seen.get(nums[r], 0) + 1

            if seen[nums[r]] == 1:
                dist_sum += nums[r]

            while dist_sum >= k:
                ans = min(ans, r - l + 1)

                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    dist_sum -= nums[l]
                    del seen[nums[l]]

                l += 1

        return ans if ans != float('inf') else -1
