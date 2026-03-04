class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        m = len(mat)
        n = len(mat[0])
        row_cnt = [0]*m
        col_cnt = [0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and row_cnt[i] == 1 and col_cnt[j] == 1:
                    cnt+=1
        return cnt
