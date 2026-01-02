class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        n = len(nums)//2
        mpp = {}
        for num in nums:
            mpp[num] = mpp.get(num,0)+1
        
        for key,value in mpp.items():

            if value==n:
                return key