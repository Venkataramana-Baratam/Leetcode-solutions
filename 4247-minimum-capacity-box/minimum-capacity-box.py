class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        n = len(capacity)

        idx = float('inf')
        ele = float('inf')

        for i in range(n):

            if capacity[i]>=itemSize and capacity[i]<ele:

                idx = i
                ele = capacity[i]
        if idx!=float('inf'):
            return idx
        else:
            return -1