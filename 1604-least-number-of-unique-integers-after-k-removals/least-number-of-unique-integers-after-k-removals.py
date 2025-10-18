class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mpp = {}
        mini = float('inf')
        for num in arr:
            mpp[num] = mpp.get(num,0)+1
        value_freq = sorted(mpp.values())
        for i in range(len(value_freq)):
            if k>=value_freq[i]:
                k-=value_freq[i]
                value_freq[i] = 0
            else:
                value_freq[i]-=k
                k = 0
                break
        cnt = sum(1 for f in value_freq if f>0)
        return cnt

