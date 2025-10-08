class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        m = len(potions)
        n = len(spells)
        potions.sort()
        for spell in spells:
            low = 0
            high = m-1
            ind = -1
            while low<=high:
                mid = (low+high)//2
                if spell*potions[mid]>=success:
                    ind = mid
                    high = mid - 1
                else:
                    low = mid + 1
            pairs.append(0 if ind==-1 else m - ind)
        return pairs