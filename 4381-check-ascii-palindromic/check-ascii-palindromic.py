class Solution:
    def isPalindromic(self, s: str) -> bool:
        

        bin = ''.join(format(ord(c) , '08b') for c in s)


        return bin == bin[::-1]