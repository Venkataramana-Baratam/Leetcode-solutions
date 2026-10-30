class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        

        def fun(number):
            a =0
            b = 1
            ans = []
            while a <= number:
                ans.append(a)
                a,b = b, a + b
        
            return ans

        res = fun(n)
        for i in range(1,len(res)-1):

            if res[i-1] + res[i] + res[i+1] == n:
                return True

        return False
