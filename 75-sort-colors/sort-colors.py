class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l1=[]
        l2=[]
        l3=[]
        for i in range(len(nums)):
            if nums[i]==0:
                l1.append(nums[i])
            elif(nums[i]==1):
                l2.append(nums[i])
            else:
                l3.append(nums[i])
        nums[:]=l1+l2+l3