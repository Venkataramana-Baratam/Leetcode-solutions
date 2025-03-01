class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        j=-1
        for k in range(len(nums)):
            if nums[k]==0:
                j=k
                break
        if j==-1:
            return nums
        for k in range(j+1,len(nums)):
            if nums[k]!=0:
                nums[k],nums[j]=nums[j],nums[k]
                j+=1
        return nums

