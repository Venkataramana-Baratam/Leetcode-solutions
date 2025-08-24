class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        r =0
        n = len(nums)
        zeros = 0
        maxi =0
        while r<n:
            if nums[r]==0:
                zeros+=1
            if zeros<=1:
                maxi = max(maxi,r-l)
            if zeros>1:
                if nums[l]==0:
                    zeros-=1
                l+=1
                maxi = max(maxi,r-l)
            r+=1
        return maxi
