class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mpp = {}
        mini = sys.maxsize
        for i in nums:
            if i%2==0:
                if i in mpp:
                    mpp[i]+=1
                else:
                    mpp[i] = 1
        max_freq = 0
        ans =-1
        if not mpp:
            return -1
        for key,value in mpp.items():
            if value > max_freq:
                max_freq = value
                ans = key
            elif value==max_freq:
                ans = min(ans,key)
        return ans