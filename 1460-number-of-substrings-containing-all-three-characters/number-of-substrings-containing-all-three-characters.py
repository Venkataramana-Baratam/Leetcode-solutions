class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        freq = {'a': 0, 'b': 0, 'c': 0}
        
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1

            while all(freq[char] > 0 for char in 'abc'):
                count += len(s) - right
                if s[left] in freq:
                    freq[s[left]] -= 1
                left += 1
        
        return count
