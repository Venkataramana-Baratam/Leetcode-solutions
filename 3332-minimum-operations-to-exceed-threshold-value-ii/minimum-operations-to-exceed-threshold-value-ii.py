import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        c=0
        while(nums[0]<k):
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_element= x*2+y
            heapq.heappush(nums,new_element)
            c+=1
        return c