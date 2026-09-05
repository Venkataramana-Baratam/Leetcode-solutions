class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        

        max_freq = 0

        mpp = {}

        for num in nums:

            mpp[num] = mpp.get(num,0) + 1
        
        for val in mpp.values():
            max_freq = max(max_freq , val)

        res = []

        for key , val in mpp.items():

            if max_freq == val:
                res.append([key,val])

        max_len = len(nums)
        for key , val in res:
            
            first = -1
            last = -1
            for i in range(len(nums)):
                if nums[i] == key:
                    if first == -1:
                        first = i
                    last = i

            max_len = min(max_len , last - first + 1)

        return max_len