class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0 
        n = len(s)
        hash = [0] * 26
        max_f = 0
        max_len = 0
        while r < n:
            hash[ord(s[r]) - ord('A')] += 1
            max_f = max(max_f, hash[ord(s[r]) - ord('A')])
            while (r - l + 1) - max_f > k:
                hash[ord(s[l]) - ord('A')] -= 1
                l += 1  
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
