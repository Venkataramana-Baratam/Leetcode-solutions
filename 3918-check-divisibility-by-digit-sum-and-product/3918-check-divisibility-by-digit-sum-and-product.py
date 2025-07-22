class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        product = 1
        for i in str(n):
            digit_sum +=int(i)
            product*=int(i)
        total_sum = digit_sum+product
        if n%total_sum==0:
            return True
        return False