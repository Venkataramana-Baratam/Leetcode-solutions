class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        

        if s == 0:
            return 0

        start = int(math.pow(10, n - 1))
        end = int(math.pow(10, n)) - 1

        
        maxi = float('-inf')
        for num in range(start,end+1):
            total = 0
            for ch in str(num):
                total+=int(ch)

            if total == s:
                maxi = max(num,maxi)
        return maxi if maxi!=float('-inf') else -1