class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n =nums[i]
            s=0
            while n!=0:
                s+=(n%10)
                n//=10
            if s==i:
                return i
        return -1