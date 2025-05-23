class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        n = len(nums)
        low = 0
        high = n-1
        l1 =[]
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]>=target:
                ans = mid
                high = mid -1
            else:
                low = mid+1
        l1.append(ans)
        anss=n
        low = 0
        high = n-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]>target:
                anss = mid
                high = mid-1
            else:
                low = mid +1
        l1.append(anss-1)
        return l1
        