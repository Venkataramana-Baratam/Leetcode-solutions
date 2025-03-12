class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k=-1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                k=i
        if k==-1:
            nums.reverse()
            return
        for i in range(len(nums)-1,k,-1):
            if nums[k]<nums[i]:
                nums[k],nums[i] = nums[i],nums[k]
                break
        i,j=k+1,len(nums)-1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
          

        