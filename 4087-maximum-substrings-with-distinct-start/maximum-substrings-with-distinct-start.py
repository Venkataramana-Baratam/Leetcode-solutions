class Solution:
    def maxDistinct(self, s: str) -> int:
        distinct = set()
        for i in s:
            distinct.add(i)
        return len(distinct)