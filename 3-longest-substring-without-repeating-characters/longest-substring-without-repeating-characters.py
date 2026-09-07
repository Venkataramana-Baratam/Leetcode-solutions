class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = [-1] * 256

        l = 0
        r = 0
        n = len(s)

        max_len = 0

        while r < n:

            if hash[ord(s[r])] != -1:

                if hash[ord(s[r])] >= l:
                    l = hash[ord(s[r])] + 1

            length = r - l + 1
            max_len = max(length, max_len)

            hash[ord(s[r])] = r

            r += 1

        return max_len