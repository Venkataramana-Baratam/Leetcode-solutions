class Solution:
    def maxFreqSum(self, s: str) -> int:
        mpp = {}
        vowels = {'a','e','i','o','u'}
        for i in s:
            mpp[i] = mpp.get(i,0)+1
        v_max = 0
        c_max = 0
        for key,value in mpp.items():
            if key in vowels:
                v_max = max(v_max,value)
            else:
                c_max = max(c_max,value)
        return v_max+c_max 