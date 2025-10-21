class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = {}
        res = []
        for num in nums:
            mpp[num] = mpp.get(num,0)+1
        for key,value in mpp.items():
            res.append((key,value))
        res.sort(key = lambda x:(x[1],x[0]),reverse = True)
        ans = [key for key,value in res[:k]]
        return ans