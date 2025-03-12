class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l1=[]
        l2=[]
        for i in range(len(nums)):
            if nums[i]>0:
                l1.append(nums[i])
            elif(nums[i]<0):
                l2.append(nums[i])
        h = len(l1)
        m=len(l2)
        return max(h,m)