
class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:

        row = 0
        col = 0

        m = len(grid)
        n = len(grid[0])

        visited = {(0, 0)}

        while True:

            ch = grid[row][col]

            nr, nc = row, col

            if ch == "L":
                nc -= 1
            elif ch == "R":
                nc += 1
            elif ch == "U":
                nr -= 1
            elif ch == "D":
                nr += 1

            if nr < 0 or nr >= m or nc < 0 or nc >= n:
                break

            if (nr, nc) in visited:
                break

            row, col = nr, nc
            visited.add((row, col))

        return [row, col]
