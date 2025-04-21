from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i]
        total = 0
        for length in range(1, n + 1, 2):
            for start in range(n - length + 1):
                end = start + length - 1
                if start == 0:
                    total += prefix[end]
                else:
                    total += prefix[end] - prefix[start - 1]

        return total
