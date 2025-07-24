class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        result = []
        for num in nums2:
            if count1[num]>0:
                result.append(num)
                count1[num]-=1
        return result