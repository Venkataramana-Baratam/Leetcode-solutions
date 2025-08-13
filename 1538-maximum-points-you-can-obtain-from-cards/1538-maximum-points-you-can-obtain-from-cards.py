class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        max_sum = 0
        n = len(cardPoints)
        for i in range(k):
            lsum += cardPoints[i]
        max_sum = lsum
        for i in range(1, k + 1):
            lsum -= cardPoints[k - i]       
            rsum += cardPoints[-i]         
            max_sum = max(max_sum, lsum + rsum)

        return max_sum
