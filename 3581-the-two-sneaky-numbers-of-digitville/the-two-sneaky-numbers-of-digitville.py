class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mpp = {}
        res= []
        for i in nums:
            mpp[i] = mpp.get(i,0)+1
        for key,value in mpp.items():
            if value==2:
                res.append(key)
        return res