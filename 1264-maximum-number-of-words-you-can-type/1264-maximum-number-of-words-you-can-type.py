class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_list = text.split()
        cnt = 0
        for word in text_list:
            if not any(ch in word for ch in brokenLetters):
                cnt += 1
        return cnt
