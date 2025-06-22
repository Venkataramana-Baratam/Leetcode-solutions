class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = {}
        for i in nums:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] =1
        sorted_items = sorted(mpp.items(), key = lambda x:x[1], reverse = True)
        res = [key for key,value in sorted_items[:k]]
        return res