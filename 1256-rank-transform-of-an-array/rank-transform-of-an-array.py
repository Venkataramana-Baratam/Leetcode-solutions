class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Step 1: Sort unique elements
        sorted_unique = sorted(set(arr))
        
        # Step 2: Assign rank to each unique element
        rank = {num: i + 1 for i, num in enumerate(sorted_unique)}
        
        # Step 3: Replace each element with its rank
        return [rank[num] for num in arr]
