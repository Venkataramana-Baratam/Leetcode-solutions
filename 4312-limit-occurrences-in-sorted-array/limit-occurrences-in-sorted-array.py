class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        
        mpp = {}

        for num in nums:

            mpp[num] = mpp.get(num,0) + 1

        res = []

        for key,value in mpp.items():

            cnt = min(k,value)

            for _ in range(cnt):
                res.append(key)
        return res