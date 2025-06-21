class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        mpp = {}
        counter = []
        for i in word:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        for key,value in mpp.items():
            counter.append(value)
        res = sys.maxsize
        for base in counter:
            deletions = 0
            for cnt in counter:
                if cnt<base:
                    deletions +=cnt
                elif cnt > base+k:
                    deletions+=cnt -(base + k )
            res = min(res,deletions)
        return res