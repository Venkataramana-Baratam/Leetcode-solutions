class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def fun(weights,capacity):
            load =0
            day =1
            for i in range(len(weights)):
                if load+weights[i]>capacity:
                    day =day+1
                    load = weights[i]
                else:
                    load+=weights[i]
            return day
        low = max(weights)
        high = sum(weights)
        while low<=high:
            mid = (low+high)//2
            ans = fun(weights,mid)
            if ans <= days:
                high = mid-1
            else:
                low =mid+1
        return low