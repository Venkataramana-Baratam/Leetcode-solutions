class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        ans = []

        while left <= right and top <= bottom:

            # 1. Traverse top row → left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])

            top += 1

            # 2. Traverse right column → top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])

            right -= 1

            # 3. Traverse bottom row → right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])

                bottom -= 1

            # 4. Traverse left column → bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])

                left += 1

        return ans