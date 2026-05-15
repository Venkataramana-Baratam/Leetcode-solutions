class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        ans = float("inf")
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                ans = min(nums[low],ans)
                low = mid + 1
            else:
                ans = min(ans,nums[mid])
                high = mid - 1
        return ans