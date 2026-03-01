class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        
        n = len(nums)

        mpp = {}

        for num in nums:

            mpp[num] = mpp.get(num,0)+1

        keys = sorted(mpp.keys())

        if len(mpp)<2:
            return [-1,-1]

        for i in range(len(keys)):
            x = keys[i]
            for j in range(i+1,len(keys)):
                y = keys[j]
                if mpp[x]!=mpp[y]:
                    return [x,y]

        return [-1,-1]