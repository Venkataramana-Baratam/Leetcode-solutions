class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        i =0
        j =0 
        res = []
        diagonal_index = 0
        while i<rows and j<cols:
            r,c = i,j
            diagonal =[]
            while r<rows and c>=0:
                diagonal.append(mat[r][c])
                r+=1
                c-=1
            if diagonal_index%2==0:
                diagonal.reverse()
            
            res.extend(diagonal)
            diagonal_index+=1

            if j<cols-1:
                j+=1
            else:
                i+=1
        return res