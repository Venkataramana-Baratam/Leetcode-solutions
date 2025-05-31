from typing import List

def find_max_index(mat: List[List[int]], n: int, m: int, col: int) -> int:
    max_value = -1
    index = -1
    for i in range(n):
        if mat[i][col] > max_value:
            max_value = mat[i][col]
            index = i
    return index

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low, high = 0, m - 1

        while low <= high:
            mid = (low + high) // 2
            max_row_index = find_max_index(mat, n, m, mid)

            left = mat[max_row_index][mid - 1] if mid - 1 >= 0 else -1
            right = mat[max_row_index][mid + 1] if mid + 1 < m else -1

            if mat[max_row_index][mid] > left and mat[max_row_index][mid] > right:
                return [max_row_index, mid]
            elif mat[max_row_index][mid] < left:
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1]
