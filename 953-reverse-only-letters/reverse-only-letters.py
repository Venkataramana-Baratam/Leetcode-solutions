class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        rev = []
        for ch in s:
            if ch.isalpha():
                rev.append(ch)

        rev.reverse()

        s = list(s)      
        j = 0            
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = rev[j]
                j += 1

        return "".join(s)
