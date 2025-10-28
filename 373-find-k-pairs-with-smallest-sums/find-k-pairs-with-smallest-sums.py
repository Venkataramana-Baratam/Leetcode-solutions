import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []
        for i in range(min(len(nums1),k)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))

        while heap and len(res)<k:

            total,i,j = heapq.heappop(heap)
            res.append([nums1[i],nums2[j]])
            if j+1<len(nums2):
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
        return res

