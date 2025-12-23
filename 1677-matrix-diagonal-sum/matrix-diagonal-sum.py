class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total+=mat[i][i]
            if i!=n-i-1:
                total+=mat[i][n-i-1]
        return total