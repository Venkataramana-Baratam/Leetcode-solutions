class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        def diag(r,c):
            i,j = r,c
            diag = []
            while i<m and j<n:
                diag.append(mat[i][j])
                i+=1
                j+=1
            diag.sort()
            for val in diag:
                mat[r][c] = val
                r+=1
                c+=1
        for i in range(m):
            diag(i,0)
        for i in range(1,n):
            diag(0,i)
        return mat