from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def lower_bound(row, x):
            low = 0
            high = len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == x:
                    return True
                elif row[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        for i in range(m):
            if lower_bound(matrix[i], target):
                return True
        return False
