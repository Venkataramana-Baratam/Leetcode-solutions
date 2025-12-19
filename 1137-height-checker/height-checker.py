class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        n = len(heights)
        cnt = 0
        expected = sorted(heights)
        for i in range(n):
            if expected[i]!=heights[i]:
                cnt+=1
        return cnt