class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mpp = {}
        ans = float('inf')

        for idx, num in enumerate(nums):
            if num in mpp:
                ans = min(ans, idx - mpp[num])
            rev = int(str(num)[::-1])
            mpp[rev] = idx

        return ans if ans != float('inf') else -1
