class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        

        cnt = nums[0]

        n = len(nums)
        for i in range(1,n):

            if nums[i] == nums[i-1] + 1:
                cnt+=nums[i]
            else:
                break
        
        while cnt in nums:
            cnt+=1

        return cnt