class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1

        high = max(piles)

        ans = float('inf')

        while low <= high:

            mid = (low + high) // 2
            req_hrs = 0
            for i in range(len(piles)):
                req_hrs+=math.ceil(piles[i] / mid)
            if req_hrs<=h:
                ans = mid

                high = mid - 1
            else:
                low = mid + 1

        return ans