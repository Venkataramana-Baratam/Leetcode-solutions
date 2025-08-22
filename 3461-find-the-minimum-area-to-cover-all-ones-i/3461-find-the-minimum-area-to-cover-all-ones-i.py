class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        top = m
        bottom = -1
        left = n
        right = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    top = min(top,i)
                    bottom = max(bottom,i)
                    left = min(left,j)
                    right = max(right,j)
        if bottom==-1:
            return 0
        return ((bottom-top)+1)*((right-left)+1)
