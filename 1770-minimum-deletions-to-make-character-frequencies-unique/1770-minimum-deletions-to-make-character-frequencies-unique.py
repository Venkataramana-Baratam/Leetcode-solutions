class Solution:
    def minDeletions(self, s: str) -> int:
        mpp = {}
        for i in s:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        seen = set()
        deletions = 0
        for freq in mpp.values():
            while freq > 0 and freq in seen:
                freq-=1
                deletions+=1
            seen.add(freq)
        return deletions