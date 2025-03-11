class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start:int):
            if start==len(nums):
                result.append(nums[:])
                return
            k=set()
            for i in range(start,len(nums)):
                if nums[i] not in k:
                    k.add(nums[i])
                    nums[start],nums[i] = nums[i],nums[start]
                    backtrack(start+1)
                    nums[start],nums[i] = nums[i],nums[start]
        result=[]
        nums.sort()
        backtrack(0)
        return result