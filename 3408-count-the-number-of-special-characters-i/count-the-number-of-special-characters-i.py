class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        upper_hash = [0] * 26
        lower_hash = [0] * 26

        for ch in word:
            if ch.isupper():
                upper_hash[ord(ch) - ord('A')] = 1
            else:
                lower_hash[ord(ch) - ord('a')] = 1

        count = 0
        for i in range(26):
            if upper_hash[i] == 1 and lower_hash[i] == 1:
                count += 1

        return count