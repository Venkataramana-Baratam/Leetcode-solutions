from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        total_sum=0
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            total_sum = sum(ceil(num/mid) for num in nums)
            if total_sum<=threshold:
                high= mid-1
            else:
                low=mid+1
        return low

