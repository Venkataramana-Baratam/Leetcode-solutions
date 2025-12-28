class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        prefixSum = [0] * n
        suffixMin = [0] * n

    
        prefixSum[0] = nums[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        
        suffixMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])

        score = [0] * n

        for i in range(n - 1):
            score[i] = prefixSum[i] - suffixMin[i + 1]

        return max(score[:n - 1])
