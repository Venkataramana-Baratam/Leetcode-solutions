class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        cnt = 0
        maxi = float('-inf')

        for num in nums:

            if num == 1:
                cnt+=1

            else:

                maxi = max(maxi,cnt)
                cnt = 0

        return max(maxi,cnt)
