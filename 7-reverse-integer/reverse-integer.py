class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversenum = 0

        while x > 0:
            reversenum = reversenum * 10 + x % 10
            x = x // 10

        reversenum *= sign

        if reversenum < -2**31 or reversenum > 2**31 - 1:
            return 0

        return reversenum
