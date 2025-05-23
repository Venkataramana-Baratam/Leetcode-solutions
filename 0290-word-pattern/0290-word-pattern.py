class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mpp={} 
        words = s.split()
        if len(pattern)!=len(words):
            return False
        for i,j in zip(words,pattern):
            if j in mpp:
                if mpp[j]!=i:
                    return False
            else:
                if i in mpp.values():
                    return False
                mpp[j] = i
        return True
