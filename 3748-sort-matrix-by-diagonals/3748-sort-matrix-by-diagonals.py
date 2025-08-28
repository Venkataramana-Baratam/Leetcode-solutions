class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        def diag(r,c,order = True):
            i,j = r,c
            diag = []
            while i<rows and j<rows:
                diag.append(grid[i][j])
                i+=1
                j+=1
            diag.sort(reverse = order)
            for val in diag:
                grid[r][c] = val
                r+=1
                c+=1
        #bottom triangle |rows
        for i in range(rows):
            diag(i,0)
        #top triangle |columns
        for j in range(1,rows):
            diag(0,j,order = False)
        return grid