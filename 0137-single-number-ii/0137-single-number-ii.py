class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mpp = {}
        for i in nums:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] =1
        for key,value in mpp.items():
            if value==1:
                return key