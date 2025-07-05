class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mpp = {}
        maxi = -1
        for  i in arr:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        for key,value in mpp.items():
            if value == key:
                maxi = max(maxi,value)
        return maxi