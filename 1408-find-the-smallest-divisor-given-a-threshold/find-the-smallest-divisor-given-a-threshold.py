class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            total = sum(math.ceil(i/mid) for i in nums)
            if total<=threshold:
                high= mid-1
            else:
                low =mid+1
        return low