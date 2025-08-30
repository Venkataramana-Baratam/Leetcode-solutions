from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        r = 0
        while r < n:  
            r_mpp = {}
            c_mpp = {}
            c = 0
            while c < n:  
                r_mpp[matrix[r][c]] = r_mpp.get(matrix[r][c], 0) + 1
                c_mpp[matrix[c][r]] = c_mpp.get(matrix[c][r], 0) + 1
                c += 1
            for num in range(1, n+1):
                if r_mpp.get(num, 0) != 1 or c_mpp.get(num, 0) != 1:
                    return False

            r += 1

        return True
