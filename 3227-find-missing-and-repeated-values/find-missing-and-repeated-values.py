class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mpp={}
        ans=0
        n=len(grid)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in mpp:
                    mpp[grid[i][j]]+=1
                else:
                    mpp[grid[i][j]]=1
        for num in range(1,(n*n)+1):
            if num not in mpp:
                missing=num
            elif mpp[num]==2:
                repeat=num
        return [repeat,missing]
            
            