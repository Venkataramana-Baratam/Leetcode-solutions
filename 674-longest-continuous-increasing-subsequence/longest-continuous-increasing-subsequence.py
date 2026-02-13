class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        cnt= 1
        maxi = 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                cnt+=1
            else:

                maxi = max(maxi,cnt)
                cnt = 1
        return max(maxi,cnt)