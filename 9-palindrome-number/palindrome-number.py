class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversenum=0
        dup =x
        while x>0:
            lastdigit=x%10
            reversenum= reversenum*10+lastdigit
            x = x//10
        if reversenum==dup:
            return True
        else:
            return False