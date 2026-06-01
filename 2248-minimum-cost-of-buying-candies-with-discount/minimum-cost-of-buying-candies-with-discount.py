class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        n = len(cost)
        if n<=2:
            return sum(cost)

        res = sorted(cost,reverse = True)

        i = 0
        total = 0
        while i<n:
            total += sum(res[i:i+2])
            i+=3
        return total
