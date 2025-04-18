class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = "1"  
        for _ in range(1, n):
            current = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                current += str(count) + result[i]  
                i += 1
            result = current  
        return result
