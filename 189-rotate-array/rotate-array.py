class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k%n
        t1 = nums[n-k:]
        t2 = nums[:n-k]
        nums[:] = t1 + t2
        