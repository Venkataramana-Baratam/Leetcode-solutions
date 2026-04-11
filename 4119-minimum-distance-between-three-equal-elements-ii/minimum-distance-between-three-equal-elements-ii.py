class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return -1
        mpp = defaultdict(list)
        for i,num in enumerate(nums):
            mpp[num].append(i)

        mini = float('inf')
        for idx in mpp.values():
            if len(idx)>=3:
                for i in range(len(idx)-2):
                    a,b,c = idx[i],idx[i+1],idx[i+2]
                    mini = min(mini,2*(c-a))
        return -1 if mini == float('inf') else mini
            