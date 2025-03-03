class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1=0
        n=len(nums)
        for i in range(1,n+1):
            xor1=xor1^i
        xor2=0
        for j in nums:
            xor2=xor2^j
        return xor1^xor2