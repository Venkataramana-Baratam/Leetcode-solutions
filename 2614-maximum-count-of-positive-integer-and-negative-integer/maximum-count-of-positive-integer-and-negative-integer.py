class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l1=[]
        l2=[]
        for i in range(len(nums)):
            if nums[i]>0:
                l1.append(nums[i])
            elif(nums[i]<0):
                l2.append(nums[i])
        return max(len(l1),len(l2))