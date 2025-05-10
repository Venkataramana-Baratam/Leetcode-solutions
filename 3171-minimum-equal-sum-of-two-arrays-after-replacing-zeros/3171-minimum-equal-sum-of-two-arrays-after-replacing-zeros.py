class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1=0
        sum2=0
        zero1=0
        zero2=0
        for i in nums1:
            sum1+=i
            if i==0:
                zero1+=1
                sum1+=1
        for j in nums2:
            sum2+=j
            if j==0:
                zero2+=1
                sum2+=1
        if sum1<sum2 and zero1==0:
            return -1
        if sum2<sum1 and zero2==0:
            return -1
        return max(sum1,sum2)