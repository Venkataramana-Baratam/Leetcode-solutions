class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums3 = sorted(nums3)
        n= len(nums3)
        median = float('inf')
        if n%2==1:
            return float(nums3[n//2])
        else:
            middle1= nums3[n//2-1]
            middle2=nums3[n//2]
            return float((middle1+middle2)/2)
