class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        mini = min(nums)
        maxi = max(nums)

        ans = []

        for num in range(mini,maxi+1):

            if num not in nums:
                ans.append(num)

        return ans