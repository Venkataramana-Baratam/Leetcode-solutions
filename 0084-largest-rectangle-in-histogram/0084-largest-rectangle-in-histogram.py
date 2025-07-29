class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = [n] * n 
        def nse(heights):
            st1 = []
            for i in range(n - 1, -1, -1):
                while st1 and heights[st1[-1]] >= heights[i]:
                    st1.pop()
                if len(st1) == 0:
                    res[i] = n  
                else:
                    res[i] = st1[-1]
                st1.append(i)
            return res
        res1 = [-1] * n  
        def pse(heights):
            st1 = []
            for i in range(n):
                while st1 and heights[st1[-1]] >= heights[i]:
                    st1.pop()
                if len(st1) == 0:
                    res1[i] = -1  
                else:
                    res1[i] = st1[-1]
                st1.append(i)
            return res1
        right = nse(heights)
        left = pse(heights)
        print(right)
        print(left)
        maxi = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            maxi = max(maxi, area)
        return maxi
