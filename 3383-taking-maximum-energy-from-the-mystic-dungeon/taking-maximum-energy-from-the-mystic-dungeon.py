class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        n = len(energy)
        maxi = float('-inf')
        for i in range(n - 1, -1, -1):
            if i + k < n:
                energy[i] += energy[i + k]
            maxi = max(maxi, energy[i])
        
        return maxi
