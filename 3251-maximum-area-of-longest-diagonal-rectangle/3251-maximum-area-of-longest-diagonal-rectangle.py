class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        m = len(dimensions)
        n = len(dimensions[0])
        maxi =0
        ans =0
        for i in range(m):
            l = dimensions[i][0]
            b = dimensions[i][1]
            res = (l**2+b**2)**0.5
            if maxi<res  or (res == maxi and l*b>ans):
                maxi = res
                ans = l*b
        return ans