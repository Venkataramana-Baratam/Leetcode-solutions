class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = {}
        for num in nums:
            rem = (num % value + value) % value 
            freq[rem] = freq.get(rem, 0) + 1
        i = 0
        while True:
            rem = i % value
            if freq.get(rem, 0) == 0: 
                return i
            freq[rem] -= 1  
            i += 1
