class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        cnt =0
        maxi = 0
        for i in range(n):
            if nums[i]==1:
                cnt+=1
                maxi = max(maxi,cnt)
            else:
                cnt =0 
        return maxi