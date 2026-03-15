class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        mpp = {}

        for num in nums:

            mpp[num] = mpp.get(num,0)+1

        for key,val in mpp.items():

            if key%2==0 and val==1:
                return key
        return -1