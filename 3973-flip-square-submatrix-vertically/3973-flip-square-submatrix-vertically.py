class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        temp = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
        s = x+k-1
        for i in range(x,x+k):
            l = y
            for j in range(y,y+k):
                temp[i][j] = grid[s][l]
                l+=1
            s-=1
        return temp

