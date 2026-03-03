class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        s1 = "0"
        def fun(x):
            if x<=1:
                return "0"
            ans = fun(x-1)
            inv = "".join(['1' if bit=='0' else '0' for bit in ans])
            return ans + "1" + inv[::-1]
        res = fun(n)
        return res[k-1]

