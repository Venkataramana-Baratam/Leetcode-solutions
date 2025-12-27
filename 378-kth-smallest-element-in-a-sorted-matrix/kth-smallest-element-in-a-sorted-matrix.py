class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        

        m, n = len(matrix), len(matrix[0])

        low, high = matrix[0][0], matrix[m-1][n-1]

        def count_less_equal(x):
            cnt = 0
            j = n - 1
            for i in range(m):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1
                cnt += (j + 1)
            return cnt

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low
