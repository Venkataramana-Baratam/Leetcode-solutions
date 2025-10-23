class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def f(y):
            if len(y)==2:
                return y[0]==y[1]
            ans = ""
            for i in range(len(y)-1):
                ans += str((int(y[i])+int(y[i+1]))%10)
            return f(ans)
        return f(s)