import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = float('-inf')
        while(low<=high):
            mid =(low+high)//2
            def fun(piles,k):
                req_hours=0
                for i in range(len(piles)):
                    req_hours += math.ceil(piles[i]/k)
                return req_hours
            total_hours = fun(piles,mid)
            if total_hours <=h:
                ans = mid
                high= mid-1
            else:
                low = mid+1
        return low