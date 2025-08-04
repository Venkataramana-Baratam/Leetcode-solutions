class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1,n-1):
            if not all(nums[i]<nums[i+1] for i in range(p)):
                continue
            for q in range(p+1,n-1):
                if all(nums[i]>nums[i+1] for i in range(p,q)) and all(nums[i]<nums[i+1] for i in range(q,n-1)):
                    return True
        return False  