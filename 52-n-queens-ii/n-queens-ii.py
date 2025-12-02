class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def issafe(row,col,board,n):

            r = row
            c = col
            while r>=0 and c>=0:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r = row
            c = col
            while c>=0:
                if board[r][c] == 'Q':
                    return False
                c-=1
            r = row
            c = col
            while r < n and c>=0:
                if board[r][c]=='Q':
                    return False
                r+=1
                c-=1
            return True
        def solve(col,board,ans,n):
            nonlocal count
            if col==n:
                count+=1
                ans.append("".join(r) for r in board)
                return 
            for row in range(n):
                if issafe(row,col,board,n):
                    board[row][col] = 'Q'
                    solve(col+1,board,ans,n)
                    board[row][col] = '.'
        ans = []
        board = [['.']*n for _ in range(n)]
        count = 0
        solve(0,board,ans,n)
        return count
