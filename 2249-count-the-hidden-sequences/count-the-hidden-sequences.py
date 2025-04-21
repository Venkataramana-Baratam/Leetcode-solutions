class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        total, maxi, mini = 0, 0, 0
        for x in differences:
            total += x
            maxi = max(maxi, total)
            mini = min(mini, total)
        return max(0, upper - lower - maxi + mini + 1)
