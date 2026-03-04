class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ones_row = [0]*m
        ones_col = [0]*n
        zeros_row = [0]*m
        zeros_col = [0]*n
        for i in range(m):
            for j in range(n):

                if grid[i][j]==1:
                    ones_row[i] += 1
                    ones_col[j] += 1

                if grid[i][j]==0:

                    zeros_row[i]+=1
                    zeros_col[j]+=1
        diff = [[0 for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
        return diff