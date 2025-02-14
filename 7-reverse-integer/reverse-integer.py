class Solution:
    def reverse(self, x: int) -> int:
        reversenum =0
        sign = -1 if x<0 else 1
        x= abs(x)
        while x>0:
            last_digit =x % 10
            x=x//10
            reversenum = (reversenum*10) + last_digit
        reversenum*=sign
        if reversenum < -2**31 or reversenum > 2**31-1:
            return 0
        return reversenum