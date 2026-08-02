class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zeros = 0
        ones = 0
        ans = 0

        for ch in s:
            if ch == '0':
                zeros += 1
            else:
                ones += 1

            if abs(zeros - ones) <= 1:
                ans += 1

        return ans
