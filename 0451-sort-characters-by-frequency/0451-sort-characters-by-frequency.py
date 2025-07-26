class Solution:
    def frequencySort(self, s: str) -> str:
        mpp = {}
        for i in s:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        sorted_char = sorted(mpp.items(),key = lambda x:-x[1])
        res = ''
        for char,value in sorted_char:
            res+=char*value
        return res