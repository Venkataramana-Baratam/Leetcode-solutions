class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n<3:
            return False
        p = -1
        for i in range(n-2):
            if nums[i]<nums[i+1]>nums[i+2]:
                p = i+1
                break
        if p==-1:
            return False
        for i in range(p):
            if nums[i]>=nums[i+1]:
                return False  
        q = -1
        for i in range(p,n-1):

            if nums[i]<nums[i+1]:
                q = i
                break
        if q==-1:
            return False
        
        
        for i in range(p,q):
            if nums[i]<=nums[i+1]:
                return False
        
        for i in range(q,n-1):
            if nums[i]>=nums[i+1]:
                return False
        return True