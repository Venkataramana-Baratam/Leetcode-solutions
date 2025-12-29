class Solution:
    def toLowerCase(self, s: str) -> str:
        lower = ''

        for ch in s:
            if 'A' <= ch <= 'Z':
                lower += chr(ord(ch) - ord('A') + ord('a'))
            else:
                lower += ch

        return lower
