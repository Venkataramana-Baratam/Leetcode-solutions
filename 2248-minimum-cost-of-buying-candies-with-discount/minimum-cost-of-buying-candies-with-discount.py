class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        

        cost.sort(reverse = True)

        n = len(cost)
        res = 0
        i = 0
        while i < n:
            res += sum(cost[i:i+2])
            i+=3
        return res