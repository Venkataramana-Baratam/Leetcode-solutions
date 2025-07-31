class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = [-1]*256
        n = len(s)
        l = 0
        r = 0
        max_len = 0
        while r < n:
            if hash[ord(s[r])] != -1:
                if hash[ord(s[r])] >= l:
                    l = hash[ord(s[r])] + 1
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            hash[ord(s[r])] = r
            r += 1
        return max_len
