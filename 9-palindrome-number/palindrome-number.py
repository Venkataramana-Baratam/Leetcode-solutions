class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = len(str(x))
        y = str(x)
        def reverse(i):
            if i>=n//2:
                return True
            if y[i]!=y[n-i-1]:
                return False
            return reverse(i+1)
        return reverse(0)