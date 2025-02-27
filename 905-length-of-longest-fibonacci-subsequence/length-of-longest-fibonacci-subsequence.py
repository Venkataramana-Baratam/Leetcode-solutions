from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        max_len = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i + 1, n):
                x, y = arr[i], arr[j]
                length = 2
                
                while x + y in num_set:
                    x, y = y, x + y
                    length += 1
                
                max_len = max(max_len, length)
        
        return max_len if max_len > 2 else 0
