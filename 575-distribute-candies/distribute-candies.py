class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyType.sort()
        n = len(candyType)
        if len(set(candyType))==1:
            return 1
        elif len(set(candyType))<=n//2:
            return len(set(candyType))
        else:
            return n//2
