class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr):
            if len(curr) == n:
                happy_strings.append(curr)
                return
            for char in 'abc':
                if not curr or curr[-1] != char:
                    backtrack(curr + char)
        
        happy_strings = []
        backtrack('')
        
        if len(happy_strings) < k:
            return ""
        return happy_strings[k - 1]
