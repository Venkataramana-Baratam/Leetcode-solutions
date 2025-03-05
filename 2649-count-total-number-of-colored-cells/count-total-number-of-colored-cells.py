class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return 1 + 4 * ((n * (n - 1)) // 2)

